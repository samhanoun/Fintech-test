
# 🚀 Rapport professionnel – Pipeline CI/CD *Fintech-test*  
*Généré à partir des artefacts fournis (tests, couverture, sécurité). Langue : français.*

---

## 1) Vue d’ensemble

- **Application** : API Flask conteneurisée, modules `app_bank/*` (app, modèles, routes). Le pipeline construit l’image, démarre l’API, exécute tests unitaires & d’intégration, produit la **couverture** et lance des **scans sécurité**.  
- **Contexte métier (étude de cas)** : modernisation DevOps d’une solution FinTech critique (transactions, comptabilité, trading), avec automatisation des tests sur toute la chaîne (unitaires → perf → sécurité).

---

## 2) Résultats des tests (JUnit)

| Suite | Tests | OK | Échecs | Skips | Temps | Détails |
|---|---:|---:|---:|---:|---:|---|
| **Unitaires** | 1 | 1 | 0 | 0 | 1.408s | `tests.unit.test_health::test_health_ok` ✔︎ |
| **Intégration** | 1 | 1 | 0 | 0 | 0.207s | `tests.integration.test_transactions_api::test_health_endpoint` ✔︎ |

> Lecture simple : la *sonde de santé* (`/health`) est couverte par un test unitaire **et** un test d’intégration — bon signal de démarrage et disponibilité.

---

## 3) Couverture de code

### 3.1 Chiffres clés

- **Couverture totale** : **50 % (114/230 lignes)**. Rapport généré le **30/09/2025 18:18 +0200**.  
- Détail par fichier :

| Fichier | Stmts | Manquantes | Couverture |
|---|---:|---:|---:|
| `app_bank/__init__.py` | 0 | 0 | **100%** |
| `app_bank/app.py` | 39 | 2 | **95%** |
| `app_bank/create_users.py` | 14 | 14 | **0%** |
| `app_bank/extensions.py` | 4 | 0 | **100%** |
| `app_bank/models.py` | 22 | 1 | **95%** |
| `app_bank/routes/auth.py` | 41 | 27 | **34%** |
| `app_bank/routes/health.py` | 6 | 0 | **100%** |
| `app_bank/routes/main.py` | 5 | 1 | **80%** |
| `app_bank/routes/transactions.py` | 99 | 71 | **28%** |
| **TOTAL** | 230 | 116 | **50%** |  

> À retenir : la **plateforme** (`app.py`, `extensions.py`, `models.py`, `health.py`) est bien couverte. Les **routes métier** (`auth.py`, `transactions.py`) sont peu testées ⇒ fort levier d’amélioration.

---

## 4) Analyse détaillée **par module & fonction**

### 4.1 `app_bank/app.py` (initialisation de l’app)

- **Fonction `create_app`** : **100 % couverte** — enregistre les blueprints (`auth`, `transactions`, `health`, `main`) et configure Flask-Login.  
- Lignes manquantes : **65–66** (bloc `if __name__ == "__main__"` : démarrage serveur).

**Traduction métier** : les tests garantissent que l’application démarre correctement **via `create_app`**, pas qu’un **process serveur** est lancé.

---

### 4.2 `app_bank/models.py` (domaine : utilisateurs & transactions)

- **Classe `User`** :  
  - `User.set_password()` : **100 % couverte** (hachage du mot de passe).  
  - `User.check_password()` : **0 % couverte** — absence de test de vérification d’un mot de passe.  
  - Couverture de la classe : **50 %**.  
- **Classe `Transaction`** : définition de champs (montant, type, timestamps), **déclarée** et couverte.

**Traduction métier** : on sait créer et hacher des mots de passe ; il manque des tests sur la vérification (`check_password`). Pour les transactions, la structure existe mais sans tests métier.

---

### 4.3 `app_bank/routes/health.py` & `main.py`

- **`/health`** : **100 % couvert** et testé (unitaire **et** intégration).  
- **`main.py`** : **80 %** (1 ligne manquante). Impact faible.

---

### 4.4 `app_bank/routes/auth.py` (authentification)

| Fonction | Rôle attendu | Couverture | Lignes manquantes |
|---|---|---:|---|
| `load_user` | Chargement utilisateur | **0%** | 10 |
| `login` | Connexion | **0%** | 15–26 |
| `logout` | Déconnexion | **0%** | 32–33 |
| `register` | Inscription | **0%** | 37–58 |

**Traduction métier** : aucun test ne prouve que l’utilisateur peut se connecter/déconnecter/s’inscrire. **Priorité #1**.

---

### 4.5 `app_bank/routes/transactions.py` (métier financier)

**Fonctions exposées** : `dashboard`, `accounting`, `transfer`, `get_balance`, `create_account`, `trading`, `buy_stock`…  
→ **Toutes à 0 %** actuellement.

| Fonction | Couverture | Exemple lignes manquantes |
|---|---:|---|
| `dashboard` | **0%** | 8 lignes |
| `accounting` | **0%** | 4 lignes |
| `transfer` | **0%** | 25 lignes |
| `get_balance` | **0%** | 4 lignes |
| `create_account` | **0%** | 15 lignes |
| `trading` | **0%** | 2 lignes |
| `buy_stock` | **0%** | 13 lignes |

**Traduction métier** : aucune garantie automatisée sur transferts, solde, création de compte, ni sur le trading. Pour une FinTech, **tests indispensables**.

---

## 5) Sécurité

### 5.1 SAST – Bandit

- **B201 – Flask debug=True** : exécution de code possible. Corriger → `debug=False` en prod.  
- **B104 – Bind 0.0.0.0** : surface réseau large. Corriger via firewall/config.

### 5.2 SCA – pip-audit

- Artefact `pip-audit.json` prévu mais non fourni → CVEs dépendances non listées.

### 5.3 Trivy

- Artefact `trivy.sarif` prévu mais non fourni → CVEs image non listées.

---

## 6) Priorités de tests

1. **Auth** : login/logout/register + cas erreur.  
2. **Transactions** : transferts corrects et erreurs (solde, comptes, montants).  
3. **Models** : tester `User.check_password`.  
4. **Sécurité** : corriger `debug=True`, exploiter `pip-audit` & `Trivy`.

---

## 7) TL;DR

- ✅ Tests passent (2/2).  
- 📊 Couverture **50 %** → dette sur `auth` et `transactions`.  
- 🛡️ Bandit : 1 **High** (debug), 1 **Medium** (bind).  
- 🧩 CVEs dépendances/image : non fournis.

---
