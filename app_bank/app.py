from flask import Flask
from dotenv import load_dotenv
import os
from extensions import db, login_manager
from models import User

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

    # Créer tables + admin par défaut
    with app.app_context():
        # Ensure DB tables exist before manipulating data
        db.create_all()
        User.query.delete()
        db.session.commit()
        
        # Créer des utilisateurs de test
        users = [
            User(username="admin", balance=1000.0),
            User(username="alice", balance=500.0),
            User(username="bob", balance=750.0),
            User(username="charlie", balance=250.0)
        ]
        
        for user in users:
            user.set_password("password123")  # Même mot de passe pour tous en test
            db.session.add(user)
        
        db.session.commit()
        print("✅ Utilisateurs de test créés !")
        print("Username: admin, alice, bob, charlie")
        print("Password: password123")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
