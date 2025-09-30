from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app import db, login_manager
from models import User

auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("transactions.dashboard"))
        else:
            flash("Identifiants invalides", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Vérifier si l'utilisateur existe déjà
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Ce nom d'utilisateur existe déjà", "danger")
            return redirect(url_for("auth.register"))
        
        # Créer le nouvel utilisateur
        from decimal import Decimal
        new_user = User(username=username, balance=Decimal('0.00'))
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash("Compte créé avec succès ! Vous pouvez maintenant vous connecter.", "success")
        return redirect(url_for("auth.login"))
    
    return render_template("register.html")