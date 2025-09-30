from extensions import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Numeric(18, 4), default=0)  # <- ajouté


    # Relation vers Transaction
    transactions = db.relationship("Transaction", backref="user", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # <-- Clé étrangère vers User
    account_id = db.Column(db.String(64), nullable=False, index=True)
    amount = db.Column(db.Numeric(18, 4), nullable=False)
    currency = db.Column(db.String(8), default="EUR", nullable=False)
    type = db.Column(db.String(8), nullable=False)  # 'credit' ou 'debit'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
