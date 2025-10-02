from flask import Flask
from dotenv import load_dotenv
import os
from extensions import db, login_manager
import time
from models import User
from sqlalchemy import text

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

    # Config DB
    db_path = os.getenv("DATABASE_URL", "sqlite:///./transactions.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialiser extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Importer routes
    from routes.auth import auth_bp
    from routes.transactions import transactions_bp
    from routes.health import health_bp
    from routes.main import main_bp




    app.register_blueprint(auth_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(main_bp)

    # Créer tables + admin par défaut (avec retry pour Postgres qui démarre)
    with app.app_context():
        retries = 0
        while True:
            try:
                db.create_all()
                break
            except Exception as e:
                retries += 1
                if retries > 30:
                    raise
                print(f"DB not ready yet, retrying ({retries})... {e}")
                time.sleep(2)

        # Lightweight in-place migration: ensure password_hash column is wide enough on Postgres
        try:
            uri = app.config.get("SQLALCHEMY_DATABASE_URI", "")
            if uri.startswith("postgresql"):
                # Check current length from information_schema; if < 200, widen to VARCHAR(255)
                with db.engine.begin() as conn:
                    current_len = conn.execute(
                        text(
                            """
                            SELECT character_maximum_length
                            FROM information_schema.columns
                            WHERE table_schema = current_schema()
                              AND table_name = 'user'
                              AND column_name = 'password_hash'
                            """
                        )
                    ).scalar()
                    if current_len is not None and current_len < 200:
                        conn.execute(text('ALTER TABLE "user" ALTER COLUMN password_hash TYPE VARCHAR(255);'))
                        print("✅ Migrated user.password_hash to VARCHAR(255)")
        except Exception as e:
            # Non-fatal; app may still work if schema already correct or on SQLite
            print(f"Schema migration check skipped/failed: {e}")

        # Seed only if database is empty
        if User.query.count() == 0:
            users = [
                User(username="admin", balance=1000.0),
                User(username="alice", balance=500.0),
                User(username="bob", balance=750.0),
                User(username="charlie", balance=250.0),
            ]
            for user in users:
                user.set_password("password123")
                db.session.add(user)
            db.session.commit()
            print("✅ Utilisateurs de test créés !")
            print("Username: admin, alice, bob, charlie")
            print("Password: password123")

    return app


if __name__ == "__main__":
    app = create_app()
    # Force debug off in container/production contexts
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
