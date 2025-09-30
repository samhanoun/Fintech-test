from app import app
from extensions import db
from models import User

with app.app_context():
    # Supprimer tous les utilisateurs existants (ATTENTION : à utiliser seulement en dev !)
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