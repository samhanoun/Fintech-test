from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db
from models import User, Transaction
from datetime import datetime
from decimal import Decimal  # ← AJOUTER CETTE LIGNE

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.route("/dashboard")
@login_required
def dashboard():
    # Récupérer les transactions
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.created_at.desc()).limit(10).all()
    
    # Calculer revenus et dépenses du mois en cours
    from datetime import datetime
    now = datetime.now()
    start_of_month = datetime(now.year, now.month, 1)
    
    monthly_transactions = Transaction.query.filter(
        Transaction.user_id == current_user.id,
        Transaction.created_at >= start_of_month
    ).all()
    
    # Calculer les totaux
    revenus = sum(t.amount for t in monthly_transactions if t.amount > 0)
    depenses = sum(abs(t.amount) for t in monthly_transactions if t.amount < 0)
    
    return render_template("dashboard.html", 
                         transactions=transactions,
                         revenus=revenus,
                         depenses=depenses)

@transactions_bp.route("/accounting")
@login_required
def accounting():
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.created_at.desc()).all()
    
    total_revenus = sum(Decimal(str(t.amount)) for t in transactions if t.amount > 0)
    total_depenses = sum(abs(Decimal(str(t.amount))) for t in transactions if t.amount < 0)
    
    return render_template("accounting.html",
                         transactions=transactions,
                         total_revenus=total_revenus,
                         total_depenses=total_depenses)


@transactions_bp.route("/transfer", methods=["GET", "POST"])
@login_required
def transfer():
    if request.method == "POST":
        to_user_id = request.form.get("to_user_id")
        amount = Decimal(request.form.get("amount"))
        description = request.form.get("description", "Virement")
        
        # Vérifications
        if amount <= 0:
            flash("Le montant doit être positif", "danger")
            return redirect(url_for("transactions.transfer"))
        
        if current_user.balance < amount:
            flash("Solde insuffisant", "danger")
            return redirect(url_for("transactions.transfer"))
        
        # Récupérer le destinataire
        to_user = User.query.get(to_user_id)
        if not to_user:
            flash("Compte destinataire introuvable", "danger")
            return redirect(url_for("transactions.transfer"))
        
        # Effectuer le virement
        current_user.balance -= amount
        to_user.balance += amount
        
        # Créer les transactions - AJOUTER account_id
        transaction_out = Transaction(
            user_id=current_user.id,
            account_id=current_user.id,  # ← AJOUTER CETTE LIGNE
            amount=-amount,
            type=f"Virement vers {to_user.username}",
            currency="EUR",
            created_at=datetime.now()
        )
        
        transaction_in = Transaction(
            user_id=to_user.id,
            account_id=to_user.id,  # ← AJOUTER CETTE LIGNE
            amount=amount,
            type=f"Virement de {current_user.username}",
            currency="EUR",
            created_at=datetime.now()
        )
        
        db.session.add(transaction_out)
        db.session.add(transaction_in)
        db.session.commit()
        
        flash(f"Virement de {amount}€ effectué avec succès vers {to_user.username}", "success")
        return redirect(url_for("transactions.dashboard"))
    
    # GET : afficher le formulaire
    users = User.query.all()
    return render_template("transfer.html", users=users)


@transactions_bp.route("/api/balance/<int:user_id>", methods=["GET"])
@login_required
def get_balance(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "Utilisateur introuvable"}, 404
    
    return {
        "user_id": user.id,
        "username": user.username,
        "balance": float(user.balance)
    }, 200

@transactions_bp.route("/create-account", methods=["GET", "POST"])
@login_required
def create_account():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        initial_balance = Decimal(request.form.get("initial_balance", 0))
        
        # Vérifier si l'utilisateur existe déjà
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Ce nom d'utilisateur existe déjà", "danger")
            return redirect(url_for("transactions.create_account"))
        
        # Créer le nouvel utilisateur
        new_user = User(username=username, balance=initial_balance)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash(f"Compte {username} créé avec succès avec un solde de {initial_balance}€", "success")
        return redirect(url_for("transactions.dashboard"))
    
    return render_template("create_account.html")


@transactions_bp.route("/trading")
@login_required
def trading():
    # Récupérer le portefeuille (à implémenter selon votre modèle)
    portfolio = []  # Pour l'instant vide
    return render_template("trading.html", portfolio=portfolio)

@transactions_bp.route("/trading/buy")
@login_required
def buy_stock():
    symbol = request.args.get('symbol')
    quantity = int(request.args.get('quantity'))
    price = Decimal(request.args.get('price'))
    total = price * quantity
    
    if current_user.balance < total:
        flash("Solde insuffisant", "danger")
        return redirect(url_for("transactions.trading"))
    
    current_user.balance -= total
    
    # Enregistrer la transaction
    transaction = Transaction(
        user_id=current_user.id,
        account_id=current_user.id,
        amount=-total,
        type=f"Achat {quantity} actions {symbol}",
        currency="EUR",
        created_at=datetime.now()
    )
    db.session.add(transaction)
    db.session.commit()
    
    flash(f"Achat de {quantity} actions {symbol} réussi!", "success")
    return redirect(url_for("transactions.trading"))