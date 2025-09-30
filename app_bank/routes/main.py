from flask import Blueprint, redirect, url_for

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    # Redirige vers le dashboard si connecté
    return redirect(url_for("transactions.dashboard"))
