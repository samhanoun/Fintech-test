# 🚀 Template de Prompt CI/CD pour VS Code Copilot

## 📋 Instructions d'utilisation

1. **Copiez le prompt ci-dessous**
2. **Remplacez tous les placeholders** entre crochets `[PLACEHOLDER]` par vos valeurs
3. **Supprimez les sections** non pertinentes pour votre projet
4. **Collez dans VS Code Copilot** pour générer votre projet

---

# PROMPT À PERSONNALISER

Je veux créer un projet **[NOM_PROJET]** avec une architecture CI/CD complète incluant les pipelines GitHub Actions, Docker, tests de performance et sécurité.

## 📦 Stack Technique

**Backend:**
- Langage: **[LANGAGE]** (ex: Python 3.11, Node.js 20, Java 17)
- Framework: **[FRAMEWORK]** (ex: Flask, Express, Spring Boot)
- ORM/Database Access: **[ORM]** (ex: SQLAlchemy, Prisma, Hibernate)

**Base de données:**
- Développement/CI: **[DB_DEV]** (ex: SQLite, H2, MongoDB Memory)
- UAT/Production: **[DB_PROD]** (ex: PostgreSQL 16, MySQL 8, MongoDB)

**Infrastructure:**
- Conteneurisation: Docker + Docker Compose
- Orchestration: **[ORCHESTRATION]** (ex: docker-compose, Kubernetes)

## 🏗️ Architecture de l'application

**Type d'application:** **[TYPE_APP]** (ex: Web App avec authentification, API REST, Microservice)

**Fonctionnalités principales:**
1. **[FEATURE_1]** (ex: Système d'authentification - login/register/logout)
2. **[FEATURE_2]** (ex: Gestion de transactions - create/read/list)
3. **[FEATURE_3]** (ex: Dashboard utilisateur avec statistiques)
4. **[FEATURE_4]** (ex: [Optionnel] Autres fonctionnalités métier)

**Routes/Endpoints principaux:**
- `GET /` - **[DESCRIPTION_ROUTE_1]** (ex: Page d'accueil)
- `GET /health` - **[DESCRIPTION_ROUTE_2]** (ex: Healthcheck endpoint)
- `POST /[ROUTE_3]` - **[DESCRIPTION_ROUTE_3]** (ex: POST /auth/register - Création compte)
- `POST /[ROUTE_4]` - **[DESCRIPTION_ROUTE_4]** (ex: POST /auth/login - Connexion)
- `GET /[ROUTE_5]` - **[DESCRIPTION_ROUTE_5]** (ex: GET /dashboard - Tableau de bord)
- `POST /[ROUTE_6]` - **[DESCRIPTION_ROUTE_6]** (ex: POST /transactions - Créer transaction)
- `GET /[ROUTE_7]` - **[DESCRIPTION_ROUTE_7]** (ex: GET /transactions - Liste transactions)

**Modèles de données:**
```
[MODELE_1]:
  - champ1: [TYPE] (ex: id: Integer, primary_key)
  - champ2: [TYPE] (ex: username: String(80), unique)
  - champ3: [TYPE] (ex: password_hash: String(255))
  - champ4: [TYPE] (ex: created_at: DateTime)

[MODELE_2]:
  - champ1: [TYPE]
  - champ2: [TYPE]
  - relation: [RELATION] (ex: foreign_key vers [MODELE_1])
```

**Exemple concret à suivre (Fintech):**
```
User:
  - id: Integer, primary_key
  - username: String(80), unique, not null
  - password_hash: String(255), not null
  - created_at: DateTime, default=now

Transaction:
  - id: Integer, primary_key
  - user_id: Integer, ForeignKey('user.id')
  - type: String(20) (deposit/withdraw/transfer)
  - amount: Float, not null
  - timestamp: DateTime, default=now
  - user: relationship(User, backref='transactions')
```

## 📁 Structure de fichiers

**Structure principale:**
```
[NOM_PROJET]/
  [APP_FOLDER]/                    (ex: app_bank, src, api)
    app.[EXT]                      (ex: app.py, server.js, main.java)
    models.[EXT]                   (ex: models.py, models.ts)
    extensions.[EXT]               (ex: extensions.py, database.ts)
    requirements.[EXT]             (ex: requirements.txt, package.json, pom.xml)
    Dockerfile
    
    routes/                        (ou controllers/, handlers/)
      [route1].[EXT]               (ex: auth.py, auth.controller.ts)
      [route2].[EXT]               (ex: transactions.py)
      [route3].[EXT]               (ex: health.py)
      main.[EXT]
    
    templates/                     (si applicable - web app)
      base.html
      [page1].html                 (ex: login.html)
      [page2].html                 (ex: dashboard.html)
    
    static/                        (si applicable)
      css/
        [style1].css
      js/
        [script1].js
    
    instance/                      (ou data/, storage/)
      [db_file]                    (ex: transactions.db pour SQLite)
  
  docker/
    docker-compose.ci.yml
    docker-compose.uat.yml
    docker-compose.prod-blue.yml
    docker-compose.prod-green.yml
  
  k6/
    perf-smoke.js
    perf-load.js
  
  tests/
    test_[module1].[EXT]          (ex: test_auth.py, auth.test.ts)
    test_[module2].[EXT]
  
  .github/
    workflows/
      ci.yml
      cd-local.yml
  
  docs/
    CI-PIPELINE.md
    CD-PIPELINE.md
```

## 🔧 Configuration des Ports

**Ports à utiliser:**
- **[PORT_CI]**: Application CI (ex: 5000)
- **[PORT_UAT_API]**: API UAT (ex: 5001)
- **[PORT_PROD_API]**: API Production (ex: 5002)
- **[PORT_UAT_DB]**: Base de données UAT (ex: 5433 pour Postgres)
- **[PORT_PROD_DB]**: Base de données Production (ex: 5434 pour Postgres)

## 🧪 Tests et Qualité

**Tests unitaires et d'intégration:**
- Framework: **[TEST_FRAMEWORK]** (ex: pytest avec pytest-cov, Jest, JUnit)
- Couverture minimale: **[COVERAGE_MIN]**% (ex: 70%)
- Commande: **[TEST_COMMAND]** (ex: `pytest --cov=app_bank --cov-report=xml`)

**Audit de sécurité des dépendances:**
- Outil: **[AUDIT_TOOL]** (ex: pip-audit, npm audit, OWASP Dependency-Check)
- Commande: **[AUDIT_COMMAND]** (ex: `pip-audit --format json > audit.json`)

**Analyse de code statique (SAST):**
- Outil: **[SAST_TOOL]** (ex: Bandit, ESLint Security, SonarQube)
- Commande: **[SAST_COMMAND]** (ex: `bandit -r app_bank -f json -o bandit.json`)

**Scan de conteneurs:**
- Outil: Trivy
- Format: SARIF pour GitHub Security
- Commande: `trivy image --format sarif -o trivy.sarif [IMAGE_NAME]`

**Test de sécurité dynamique (DAST):**
- Outil: OWASP ZAP
- Mode: Baseline scan
- Cible: `http://localhost:[PORT_CI]`

## 🚦 Tests de performance k6

**Test Smoke (validation rapide):**
- Virtual Users: **[SMOKE_VU]** (ex: 1)
- Durée: **[SMOKE_DURATION]** (ex: 10s)
- Endpoints testés: **[SMOKE_ENDPOINTS]** (ex: GET /health)
- Seuils:
  - `http_req_duration`: p(95) < **[SMOKE_P95]**ms (ex: 500)
  - `http_req_failed`: rate < **[SMOKE_ERROR_RATE]**% (ex: 5)

**Test Load (charge réaliste):**
- Virtual Users: Progression de **[LOAD_VU_START]** à **[LOAD_VU_MAX]** (ex: 0 → 40 VUs)
- Durée totale: **[LOAD_DURATION]** (ex: ~3min avec stages)
- Stages recommandés:
  ```javascript
  stages: [
    { duration: '15s', target: [VU_20] },  // Montée progressive
    { duration: '30s', target: [VU_20] },  // Plateau
    { duration: '30s', target: [VU_40] },  // Montée pic
    { duration: '15s', target: 0 },        // Descente
  ]
  ```
- Parcours utilisateur:
  1. **[LOAD_STEP_1]** (ex: GET /health - healthcheck)
  2. **[LOAD_STEP_2]** (ex: POST /auth/register - créer compte une fois par VU)
  3. **[LOAD_STEP_3]** (ex: POST /auth/login - se connecter)
  4. **[LOAD_STEP_4]** (ex: GET /dashboard - accéder au dashboard)
  5. **[LOAD_STEP_5]** (ex: [Optionnel] Autres actions métier)
- Seuils adaptés:
  - `http_req_duration`: p(95) < **[LOAD_P95]**ms (ex: 800)
  - `http_req_failed`: rate < **[LOAD_ERROR_RATE]**% (ex: 20)

**Optimisations base de données (si SQLite en CI):**
- Journal mode: WAL
- Busy timeout: **[DB_TIMEOUT]**ms (ex: 5000)
- Configuration: `check_same_thread=False` + `SQLALCHEMY_ENGINE_OPTIONS`

## 🔄 Pipeline CI (GitHub Actions)

**Déclenchement:**
- Push sur branche: **[CI_BRANCHES]** (ex: main, develop)
- Pull requests vers: **[CI_PR_BRANCHES]** (ex: main)

**Étapes CI:**
1. **Checkout code** (actions/checkout@v4)
2. **Setup language** (ex: actions/setup-python@v5 avec version **[LANGUAGE_VERSION]**)
3. **Install dependencies** (commande: **[INSTALL_CMD]**)
4. **Build Docker images** (docker-compose -f docker/docker-compose.ci.yml build)
5. **Start services** (docker-compose up -d)
6. **Wait for health** (healthcheck sur `http://localhost:[PORT_CI]/health`)
7. **Run unit tests** (**[TEST_COMMAND]**)
8. **Security audit** (**[AUDIT_COMMAND]**)
9. **SAST scan** (**[SAST_COMMAND]**)
10. **Container scan** (Trivy SARIF)
11. **DAST scan** (ZAP Baseline)
12. **k6 Smoke test** (grafana/k6:0.51.0)
13. **k6 Load test** (grafana/k6:0.51.0 avec -u 0:0 pour permissions)
14. **Upload artifacts**: coverage, audits, scans, k6 summaries, ZAP report

**Artifacts produits:**
- `coverage.xml`
- `audit.json`
- `bandit.json` (ou équivalent SAST)
- `trivy.sarif`
- `zap-report.html`
- `k6-summary-smoke.json`
- `k6-summary-load.json`

## 🚀 Pipeline CD (Déploiement Local)

**Déclenchement:**
- **UAT (auto)**: Push sur branche **[CD_UAT_BRANCH]** (ex: main)
- **Production (manuel)**: Push de tags **[CD_PROD_TAG_PATTERN]** (ex: v*) + gate d'approbation

**Environnements:**

### UAT (User Acceptance Testing)
- Runner: **[RUNNER_TYPE]** (ex: self-hosted avec WSL2 Ubuntu)
- Mode déploiement: **[UAT_MODE]** (ex: MODE=build ou MODE=image)
- Compose: `docker/docker-compose.uat.yml`
- Ports: **[PORT_UAT_API]** (API), **[PORT_UAT_DB]** (Database)
- Accès: `http://localhost:[PORT_UAT_API]`
- Base de données: **[DB_PROD]** (ex: PostgreSQL 16)

### Production (Blue/Green)
- Runner: **[RUNNER_TYPE]** (ex: self-hosted)
- Mode déploiement: **[PROD_MODE]** (ex: MODE=build par défaut)
- Compose: `docker/docker-compose.prod-blue.yml` + `prod-green.yml`
- Stratégie: Blue/Green deployment
- Ports: **[PORT_PROD_API]** (API), **[PORT_PROD_DB]** (Database)
- Accès: `http://localhost:[PORT_PROD_API]`
- Base de données: **[DB_PROD]** (ex: PostgreSQL 16)
- Approbation: Gate manuelle avant déploiement

**Modes de déploiement:**
- `MODE=build`: Build l'image à partir du Dockerfile (plus lent, toujours à jour)
- `MODE=image`: Pull image depuis registry (rapide, nécessite push préalable)

**Étapes CD:**
1. **Checkout code**
2. **Set environment** (UAT ou PROD selon trigger)
3. **Stop old containers** (docker-compose down)
4. **Deploy new version** (docker-compose up -d avec MODE choisi)
5. **Health check** (vérification `http://localhost:[PORT]/health`)
6. **Smoke test post-deploy** (k6 rapide ou curl)

**Rollback:**
- Si MODE=image: `docker-compose pull [VERSION_PRECEDENTE]` puis up
- Si MODE=build: `git revert` puis re-trigger pipeline
- Blue/Green: Basculer vers l'autre couleur (swap profiles)

## 📊 Documentation

**Créer deux documents détaillés:**

### `CI-PIPELINE.md`
Sections:
1. Vue d'ensemble
2. Prérequis
3. Architecture
4. Étapes détaillées (Build, Tests, Scans, k6)
5. Artifacts et rapports
6. Troubleshooting
7. Comparaison k6 smoke vs load

### `CD-PIPELINE.md`
Sections:
1. Vue d'ensemble
2. Prérequis (self-hosted runner, Docker, WSL2)
3. Déclenchement (push main pour UAT, tags v* pour Prod)
4. Environnements (UAT vs Prod)
5. Modes de déploiement (image vs build)
6. Étapes détaillées
7. Accès aux applications (URLs, ports)
8. Rollback et récupération
9. Troubleshooting

## 🔐 Sécurité et Secrets

**Secrets GitHub requis:**
- **[SECRET_1]**: **[DESCRIPTION]** (ex: DOCKERHUB_USERNAME)
- **[SECRET_2]**: **[DESCRIPTION]** (ex: DOCKERHUB_TOKEN)
- **[SECRET_3]**: **[DESCRIPTION]** (ex: DATABASE_PASSWORD)
- **[SECRET_4]**: **[DESCRIPTION]** (ex: [Optionnel] API keys tierces)

**Variables d'environnement:**
```yaml
[VAR_1]: [VALEUR]  # ex: DATABASE_URL: postgresql://user:pass@db:5432/dbname
[VAR_2]: [VALEUR]  # ex: SECRET_KEY: ${SECRET_KEY}
[VAR_3]: [VALEUR]  # ex: FLASK_ENV: production
```

## 🐳 Configuration Docker

**Dockerfile pour l'application:**
```dockerfile
FROM [BASE_IMAGE]:[VERSION]    # ex: python:3.11-slim

WORKDIR /app

# Dépendances
COPY requirements.[EXT] .      # ex: requirements.txt, package.json
RUN [INSTALL_COMMAND]          # ex: pip install --no-cache-dir -r requirements.txt

# Code application
COPY [APP_FOLDER]/ ./[APP_FOLDER]/

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD [HEALTHCHECK_CMD]        # ex: curl -f http://localhost:5000/health || exit 1

# Exposer port
EXPOSE [PORT]

# Commande de démarrage
CMD [START_COMMAND]            # ex: ["python", "app_bank/app.py"]
```

**Docker Compose services:**
```yaml
services:
  web:
    build: .
    ports:
      - "[HOST_PORT]:[CONTAINER_PORT]"
    environment:
      DATABASE_URL: [DB_CONNECTION_STRING]
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: [HEALTHCHECK_CMD]
      interval: 10s
      timeout: 5s
      retries: 5
  
  db:
    image: [DB_IMAGE]:[VERSION]  # ex: postgres:16-alpine
    environment:
      [DB_ENV_VARS]              # ex: POSTGRES_PASSWORD, POSTGRES_DB
    ports:
      - "[DB_HOST_PORT]:[DB_CONTAINER_PORT]"
    volumes:
      - [VOLUME_NAME]:/var/lib/[db_type]/data
    healthcheck:
      test: [DB_HEALTHCHECK]     # ex: pg_isready -U user
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  [VOLUME_NAME]:
```

## ✅ Checklist de génération

Génère le projet avec:

- [ ] Structure de fichiers complète selon `[NOM_PROJET]/[APP_FOLDER]/`
- [ ] Code de l'application avec modèles **[MODELE_1]**, **[MODELE_2]**
- [ ] Routes/endpoints: **[ROUTE_3]**, **[ROUTE_4]**, **[ROUTE_5]**, etc.
- [ ] Tests unitaires avec **[TEST_FRAMEWORK]** (couverture > **[COVERAGE_MIN]**%)
- [ ] Scripts k6 (smoke + load) adaptés aux endpoints
- [ ] Dockerfiles + docker-compose (ci, uat, prod-blue, prod-green)
- [ ] Workflow CI GitHub Actions (11+ étapes)
- [ ] Workflow CD GitHub Actions (UAT auto + Prod gate)
- [ ] Documentation `CI-PIPELINE.md` et `CD-PIPELINE.md` en français
- [ ] Healthchecks sur tous les services
- [ ] Gestion des secrets et variables d'environnement
- [ ] Configuration base de données (SQLite/CI + Postgres/UAT-Prod)
- [ ] Migration auto de schéma (password_hash VARCHAR(255) pour Postgres)
- [ ] Optimisations SQLite (WAL, busy_timeout) si applicable
- [ ] Artifacts CI (coverage, scans, k6 summaries)
- [ ] Scripts de rollback et troubleshooting
- [ ] `.gitignore` adapté (**[LANGUAGE]**, Docker, IDE)

## 🎯 Résultat attendu

Un projet **[NOM_PROJET]** production-ready avec:
- ✅ Pipeline CI complet (build, test, scan, perf) sur GitHub Actions
- ✅ Pipeline CD avec UAT auto et Prod gated, déploiement Blue/Green
- ✅ Tests de performance k6 (smoke + load réaliste)
- ✅ Scans de sécurité multi-niveaux (SCA, SAST, Container, DAST)
- ✅ Documentation détaillée en français
- ✅ Architecture scalable et maintenable
- ✅ Prêt pour déploiement local ou cloud

---

## 📝 Exemple de valeurs (Fintech)

Pour référence, voici les valeurs utilisées dans le projet Fintech d'origine:

```
[NOM_PROJET] = Fintech-test
[LANGAGE] = Python 3.11
[FRAMEWORK] = Flask
[ORM] = SQLAlchemy
[DB_DEV] = SQLite
[DB_PROD] = PostgreSQL 16
[TYPE_APP] = Web App avec authentification et gestion de transactions
[APP_FOLDER] = app_bank
[PORT_CI] = 5000
[PORT_UAT_API] = 5001
[PORT_PROD_API] = 5002
[PORT_UAT_DB] = 5433
[PORT_PROD_DB] = 5434
[TEST_FRAMEWORK] = pytest
[COVERAGE_MIN] = 70
[SMOKE_VU] = 1
[SMOKE_DURATION] = 10s
[LOAD_VU_MAX] = 40
[LOAD_P95] = 800
[RUNNER_TYPE] = self-hosted (WSL2 Ubuntu)
```

---

**💡 Astuce:** Commencez par remplir les sections principales ([NOM_PROJET], [LANGAGE], [FRAMEWORK]), puis affinez les détails (routes, modèles, ports) au fur et à mesure.

---
---
---

# 🏦 PROMPT COMPLET - PROJET FINTECH (Exemple pré-rempli)

> **Note:** Copiez ce prompt tel quel dans VS Code Copilot pour recréer le projet Fintech complet avec CI/CD.

---

Je veux créer un projet **Fintech-test** avec une architecture CI/CD complète incluant les pipelines GitHub Actions, Docker, tests de performance et sécurité.

## 📦 Stack Technique

**Backend:**
- Langage: **Python 3.11**
- Framework: **Flask** (web framework léger)
- ORM/Database Access: **SQLAlchemy** (ORM SQL + Flask-SQLAlchemy)
- Authentification: **Flask-Login** (gestion des sessions utilisateur)

**Base de données:**
- Développement/CI: **SQLite** (fichier `instance/transactions.db`)
- UAT/Production: **PostgreSQL 16** (Alpine)

**Infrastructure:**
- Conteneurisation: Docker + Docker Compose
- Orchestration: docker-compose (configurations séparées pour CI, UAT, Prod Blue/Green)

## 🏗️ Architecture de l'application

**Type d'application:** Web App avec authentification et gestion de transactions bancaires

**Fonctionnalités principales:**
1. **Système d'authentification** - Inscription, connexion, déconnexion, gestion de session
2. **Gestion de transactions** - Créer des transactions (deposit, withdraw, transfer), consulter l'historique
3. **Dashboard utilisateur** - Vue d'ensemble du compte, statistiques, solde
4. **Pages métier** - Accounting et Trading (placeholders pour futures fonctionnalités)

**Routes/Endpoints principaux:**
- `GET /` - Page d'accueil (redirect vers login ou dashboard selon session)
- `GET /health` - Healthcheck endpoint (retourne status + version)
- `POST /auth/register` - Création de compte utilisateur
- `POST /auth/login` - Connexion utilisateur (session Flask)
- `GET /auth/logout` - Déconnexion utilisateur
- `GET /dashboard` - Tableau de bord utilisateur (nécessite authentification)
- `POST /transactions/create` - Créer une transaction (deposit/withdraw/transfer)
- `GET /transactions/list` - Liste des transactions de l'utilisateur connecté
- `GET /accounting` - Page accounting (placeholder)
- `GET /trading` - Page trading (placeholder)

**Modèles de données:**

```python
User:
  - id: Integer, primary_key=True
  - username: String(80), unique=True, nullable=False
  - password_hash: String(255), nullable=False
  - created_at: DateTime, default=datetime.utcnow
  - transactions: relationship('Transaction', backref='user', lazy=True)

Transaction:
  - id: Integer, primary_key=True
  - user_id: Integer, ForeignKey('user.id'), nullable=False
  - type: String(20), nullable=False  # 'deposit', 'withdraw', 'transfer'
  - amount: Float, nullable=False
  - timestamp: DateTime, default=datetime.utcnow
  - description: String(200), nullable=True
```

## 📁 Structure de fichiers

```
Fintech-test-main/
  app_bank/
    app.py                       # Application Flask factory + config
    models.py                    # User et Transaction models (SQLAlchemy)
    extensions.py                # db, login_manager, bcrypt instances
    create_users.py              # Script pour créer utilisateurs de test
    requirements.txt             # Dépendances Python
    Dockerfile                   # Image Python 3.11-slim
    
    routes/
      __init__.py
      auth.py                    # Routes: /auth/register, /auth/login, /auth/logout
      transactions.py            # Routes: /transactions/create, /transactions/list
      health.py                  # Route: /health (healthcheck)
      main.py                    # Routes: /, /dashboard, /accounting, /trading
    
    templates/                   # Templates Jinja2
      base.html                  # Template de base avec navbar
      login.html                 # Page de connexion
      register.html              # Page d'inscription
      dashboard.html             # Dashboard utilisateur
      transactions.html          # Liste des transactions
      transfer.html              # Formulaire de transfert
      accounting.html            # Page accounting
      trading.html               # Page trading
      create_account.html        # Création de compte
    
    static/
      style.css                  # Styles globaux
      css/
        login.css                # Styles page login
        dashboard.css            # Styles dashboard
    
    instance/
      transactions.db            # Base SQLite (dev/CI uniquement)
  
  docker/
    docker-compose.ci.yml        # Config CI (SQLite)
    docker-compose.uat.yml       # Config UAT (PostgreSQL, port 5001/5433)
    docker-compose.prod-blue.yml # Config Prod Blue (PostgreSQL, port 5002/5434)
    docker-compose.prod-green.yml # Config Prod Green (PostgreSQL, port 5002/5434)
  
  k6/
    perf-smoke.js                # Test smoke: 1 VU, 10s, GET /health
    perf-load.js                 # Test load: 0→40 VUs, parcours complet (register→login→dashboard)
  
  tests/
    test_auth.py                 # Tests unitaires authentification
    test_transactions.py         # Tests unitaires transactions
    test_health.py               # Test healthcheck
    conftest.py                  # Fixtures pytest (app, client, db)
  
  .github/
    workflows/
      ci.yml                     # Pipeline CI (build, tests, scans, k6)
      cd-local.yml               # Pipeline CD (UAT auto + Prod gated)
  
  docs/
    CI-PIPELINE.md               # Documentation CI en français
    CD-PIPELINE.md               # Documentation CD en français
    PROMPT-TEMPLATE-CICD.md      # Ce fichier template
  
  .gitignore                     # Python, Docker, IDE, SQLite
  README.md                      # Documentation projet
```

## 🔧 Configuration des Ports

**Ports à utiliser:**
- **5000**: Application CI (docker-compose.ci.yml)
- **5001**: API UAT (docker-compose.uat.yml)
- **5002**: API Production (docker-compose.prod-blue/green.yml)
- **5433**: PostgreSQL UAT (docker-compose.uat.yml)
- **5434**: PostgreSQL Production (docker-compose.prod-blue/green.yml)

## 🧪 Tests et Qualité

**Tests unitaires et d'intégration:**
- Framework: **pytest** avec **pytest-cov** (coverage XML)
- Couverture minimale: **70%** (configurable)
- Commande: `pytest --cov=app_bank --cov-report=xml --cov-report=term-missing`
- Fichiers de test:
  - `test_auth.py`: Tests inscription, login, logout, validation passwords
  - `test_transactions.py`: Tests création transactions, listing, validation montants
  - `test_health.py`: Test endpoint /health
  - `conftest.py`: Fixtures (app avec config test, client Flask, db en mémoire)

**Audit de sécurité des dépendances:**
- Outil: **pip-audit** (scan des vulnérabilités CVE dans requirements.txt)
- Commande: `pip-audit --format json --output audit.json`
- Seuil: Fail si vulnérabilités critiques détectées

**Analyse de code statique (SAST):**
- Outil: **Bandit** (scan de sécurité Python)
- Commande: `bandit -r app_bank -f json -o bandit.json`
- Détecte: Hardcoded passwords, SQL injection, insecure functions, etc.

**Scan de conteneurs:**
- Outil: **Trivy** (Aqua Security)
- Format: SARIF pour GitHub Security tab
- Commande: `trivy image --format sarif --output trivy.sarif fintech-test:latest`
- Scan: OS packages + Python dependencies dans l'image Docker

**Test de sécurité dynamique (DAST):**
- Outil: **OWASP ZAP** (Zed Attack Proxy)
- Mode: Baseline scan (passif + spider)
- Cible: `http://localhost:5000`
- Commande: `zap-baseline.py -t http://localhost:5000 -r zap-report.html`
- Détecte: XSS, CSRF, headers sécurité manquants, cookies non sécurisés

## 🚦 Tests de performance k6

**Test Smoke (validation rapide):**
- Virtual Users: **1**
- Durée: **10s**
- Endpoints testés: `GET /health` (simple healthcheck)
- Seuils:
  - `http_req_duration`: p(95) < **500ms**
  - `http_req_failed`: rate < **5%**
- Objectif: Vérifier que l'application répond sous charge minimale
- Script: `k6/perf-smoke.js`
- Artifact: `k6-summary-smoke.json`

**Test Load (charge réaliste):**
- Virtual Users: Progression de **0** à **40 VUs**
- Durée totale: **~3 minutes**
- Stages:
  ```javascript
  stages: [
    { duration: '15s', target: 20 },  // Montée progressive à 20 VUs
    { duration: '30s', target: 20 },  // Plateau 20 VUs
    { duration: '30s', target: 40 },  // Montée pic à 40 VUs
    { duration: '30s', target: 40 },  // Maintien pic 40 VUs
    { duration: '30s', target: 20 },  // Descente à 20 VUs
    { duration: '15s', target: 0 },   // Descente complète
  ]
  ```
- Parcours utilisateur réaliste:
  1. `GET /health` - Healthcheck
  2. `POST /auth/register` - **Inscription une seule fois par VU** (if `__ITER === 0`)
  3. `POST /auth/login` - Connexion (chaque itération)
  4. `GET /dashboard` - Accès dashboard avec session
  5. Gestion des cookies de session Flask entre les requêtes
- Seuils adaptés (plus permissifs que smoke):
  - `http_req_duration`: p(95) < **800ms**
  - `http_req_failed`: rate < **10%** (register), < **20%** (autres)
- Objectif: Simuler charge réelle avec concurrence sur SQLite (CI)
- Script: `k6/perf-load.js`
- Artifact: `k6-summary-load.json`

**Optimisations base de données (SQLite en CI):**
- **Journal mode: WAL** (Write-Ahead Logging) pour meilleure concurrence
  ```python
  @event.listens_for(Engine, "connect")
  def set_sqlite_pragma(dbapi_conn, connection_record):
      cursor = dbapi_conn.cursor()
      cursor.execute("PRAGMA journal_mode=WAL")
      cursor.close()
  ```
- **Busy timeout: 5000ms** pour retry en cas de lock
  ```python
  SQLALCHEMY_ENGINE_OPTIONS = {
      'connect_args': {
          'check_same_thread': False,
          'timeout': 5
      }
  }
  ```
- **check_same_thread=False**: Autorise multi-threading avec SQLite

**Note k6 permissions:**
- Conteneurs k6 doivent tourner en root (`-u 0:0`) pour écrire `k6-summary.json`
- Résout erreur: `open /scripts/k6-summary.json: permission denied`

## 🔄 Pipeline CI (GitHub Actions)

**Déclenchement:**
- Push sur branche: **main**
- Pull requests vers: **main**

**Runner:** `ubuntu-latest` (GitHub-hosted)

**Étapes CI:**

1. **Checkout code** (`actions/checkout@v4`)
2. **Setup Python 3.11** (`actions/setup-python@v5`)
3. **Install dependencies** (`pip install -r app_bank/requirements.txt`)
4. **Lint/Format check** (optionnel: `flake8`, `black --check`)
5. **Build Docker images** (`docker-compose -f docker/docker-compose.ci.yml build`)
6. **Start services** (`docker-compose -f docker/docker-compose.ci.yml up -d`)
7. **Wait for health** (retry `curl http://localhost:5000/health` jusqu'à 200 OK)
8. **Run unit tests** (`pytest --cov=app_bank --cov-report=xml`)
9. **Upload coverage** (`codecov/codecov-action@v3` ou artifact)
10. **Security audit** (`pip-audit --format json -o audit.json`)
11. **SAST scan** (`bandit -r app_bank -f json -o bandit.json`)
12. **Build final image** (tag `fintech-test:latest`)
13. **Container scan** (`trivy image --format sarif -o trivy.sarif fintech-test:latest`)
14. **Upload SARIF** (`github/codeql-action/upload-sarif@v3` → Security tab)
15. **DAST scan** (`docker run zaproxy/zap-stable zap-baseline.py -t http://host.docker.internal:5000`)
16. **k6 Smoke test** (`docker run -u 0:0 grafana/k6:0.51.0 run /scripts/perf-smoke.js`)
17. **k6 Load test** (`docker run -u 0:0 grafana/k6:0.51.0 run /scripts/perf-load.js`)
    - **Toujours exécuté** même si étapes précédentes échouent (pour diagnostics)
18. **Cleanup** (`docker-compose -f docker/docker-compose.ci.yml down -v`)
19. **Upload artifacts**:
    - `coverage.xml`
    - `audit.json`
    - `bandit.json`
    - `trivy.sarif`
    - `zap-report.html`
    - `k6-summary-smoke.json`
    - `k6-summary-load.json`

**Artifacts produits:**
- **coverage.xml**: Rapport de couverture de tests (format Cobertura)
- **audit.json**: Vulnérabilités dépendances Python (pip-audit)
- **bandit.json**: Issues de sécurité code Python (SAST)
- **trivy.sarif**: Vulnérabilités image Docker (SARIF pour GitHub)
- **zap-report.html**: Scan DAST OWASP ZAP
- **k6-summary-smoke.json**: Métriques k6 smoke test
- **k6-summary-load.json**: Métriques k6 load test

**Durée estimée:** 8-12 minutes

## 🚀 Pipeline CD (Déploiement Local)

**Déclenchement:**
- **UAT (automatique)**: Push sur branche **main** (après succès CI)
- **Production (manuel)**: Push de tags **v*** (ex: v1.0.0, v2.1.3) + gate d'approbation GitHub

**Environnements:**

### UAT (User Acceptance Testing)
- **Runner**: `self-hosted` (WSL2 Ubuntu recommandé)
- **Mode déploiement**: `MODE=build` (par défaut, build depuis Dockerfile)
- **Compose**: `docker/docker-compose.uat.yml`
- **Ports**: 
  - API: **5001** (`http://localhost:5001`)
  - Database: **5433** (PostgreSQL)
- **Base de données**: PostgreSQL 16 Alpine
- **Variables**:
  ```yaml
  DATABASE_URL: postgresql://uat_user:uat_password@db:5432/uat_fintech
  FLASK_ENV: development
  SECRET_KEY: uat-secret-key-change-in-prod
  ```
- **Healthcheck**: `curl -f http://localhost:5001/health || exit 1`
- **Déploiement**: Automatique sur push main (après CI passed)

### Production (Blue/Green)
- **Runner**: `self-hosted` (WSL2 Ubuntu)
- **Mode déploiement**: `MODE=build` (par défaut, ou `MODE=image` si registry utilisé)
- **Compose**: `docker/docker-compose.prod-blue.yml` + `prod-green.yml`
- **Stratégie**: Blue/Green deployment (swap entre blue et green)
- **Ports**:
  - API: **5002** (`http://localhost:5002`)
  - Database: **5434** (PostgreSQL)
- **Base de données**: PostgreSQL 16 Alpine (volume persistant)
- **Variables**:
  ```yaml
  DATABASE_URL: postgresql://prod_user:prod_password@db:5432/prod_fintech
  FLASK_ENV: production
  SECRET_KEY: ${PROD_SECRET_KEY}  # GitHub Secret
  ```
- **Approbation**: Gate manuelle GitHub (environment protection rule)
- **Déploiement**: Trigger par tag `v*` (ex: `git tag -a v1.0.0 -m "Release 1.0.0" && git push origin v1.0.0`)

**Modes de déploiement:**
- **`MODE=build`**: 
  - Build l'image à partir du Dockerfile local
  - Plus lent (~2-3 min)
  - Toujours à jour avec le code source
  - Recommandé pour UAT et small teams
  
- **`MODE=image`**: 
  - Pull image depuis registry (DockerHub, ACR, ECR)
  - Rapide (~30s)
  - Nécessite push préalable vers registry
  - Recommandé pour Production avec CI/CD avancé

**Étapes CD (UAT ou PROD):**

1. **Checkout code** (`actions/checkout@v4`)
2. **Set environment variables**:
   - Si push main → `ENV=uat`, `MODE=build`
   - Si push tag v* → `ENV=prod`, `MODE=build` (ou image si configuré)
   - Utilise `$GITHUB_ENV` pour éviter `inputs.*` sur push events
3. **Stop old containers**:
   ```bash
   docker-compose -f docker/docker-compose.$ENV.yml down
   ```
4. **Pull/Build new version**:
   - Si `MODE=image`: `docker-compose pull`
   - Si `MODE=build`: `docker-compose build` (défaut)
5. **Start new containers**:
   ```bash
   docker-compose -f docker/docker-compose.$ENV.yml up -d
   ```
6. **Wait for health**:
   ```bash
   timeout 60 bash -c 'until curl -f http://localhost:$PORT/health; do sleep 2; done'
   ```
7. **Smoke test post-deploy**:
   - k6 smoke rapide sur nouveau déploiement
   - Vérifier login/dashboard fonctionne
8. **Notification** (optionnel: Slack, Teams, email)

**Blue/Green specifics (Prod uniquement):**
- Deux stacks complètes: `prod-blue` et `prod-green`
- Swap via profiles Docker Compose ou load balancer
- Rollback instantané en rebasculant vers ancienne couleur

**Rollback:**
- **Si MODE=image**: 
  ```bash
  # Revenir à version précédente
  docker-compose -f docker/docker-compose.prod.yml pull fintech-test:v1.0.0
  docker-compose up -d
  ```
- **Si MODE=build**: 
  ```bash
  # Git revert puis re-trigger pipeline
  git revert <commit_sha>
  git push origin main  # Re-trigger UAT
  # ou
  git tag -a v1.0.1 -m "Rollback hotfix"
  git push origin v1.0.1  # Re-trigger Prod
  ```
- **Blue/Green**: 
  ```bash
  # Swap immédiat vers ancienne stack
  docker-compose -f docker/docker-compose.prod-green.yml down
  docker-compose -f docker/docker-compose.prod-blue.yml up -d
  ```

## 📊 Documentation

**Créer deux documents détaillés en français:**

### `CI-PIPELINE.md` (Documentation Pipeline CI)

**Sections:**
1. **Vue d'ensemble**: Objectif du pipeline CI, technologies utilisées
2. **Prérequis**: Docker, Python 3.11, GitHub Actions
3. **Architecture**: Schéma du flux CI (build → test → scan → perf)
4. **Déclencheurs**: Push main, Pull Requests
5. **Étapes détaillées**:
   - 5.1 Checkout & Setup
   - 5.2 Build & Start services
   - 5.3 Healthcheck
   - 5.4 Tests unitaires (pytest + coverage)
   - 5.5 Audit sécurité (pip-audit)
   - 5.6 SAST (Bandit)
   - 5.7 Scan conteneur (Trivy SARIF)
   - 5.8 DAST (OWASP ZAP)
   - 5.9 k6 Smoke test
   - 5.9 bis k6 Load test (parcours complet, 40 VUs, SQLite WAL)
   - 5.10 Upload artifacts
6. **Artifacts et rapports**: Description de chaque artifact, où les trouver
7. **Interprétation des résultats**: Seuils, métriques importantes
8. **Configuration SQLite pour k6**: WAL mode, busy_timeout, pourquoi
9. **Troubleshooting**: Erreurs communes et solutions
10. **Variables d'environnement**: DATABASE_URL, FLASK_ENV, SECRET_KEY
11. **Optimisations possibles**: Cache dependencies, parallel jobs
12. **Intégration avec CD**: Comment CI trigger UAT
13. **Comparaison rapide: k6 smoke vs k6 load**:
    - Tableau comparatif: Portée, Intensité, Risques détectés, Seuils, Sorties

### `CD-PIPELINE.md` (Documentation Pipeline CD)

**Sections:**
1. **Vue d'ensemble**: Objectif CD, stratégie Blue/Green
2. **Prérequis**: Self-hosted runner (WSL2), Docker, accès GitHub Secrets
3. **Déclenchement**:
   - UAT: Push automatique sur main (après CI)
   - Prod: Push tags v* + approbation manuelle
4. **Environnements**:
   - 4.1 UAT: Port 5001, PostgreSQL 5433, auto-deploy
   - 4.2 Prod: Port 5002, PostgreSQL 5434, Blue/Green, approval gate
5. **Modes de déploiement**:
   - MODE=image vs MODE=build
   - Quand utiliser chaque mode
   - Configuration dans workflow
6. **Étapes détaillées**: Stop → Pull/Build → Start → Health → Test
7. **Accès aux applications**:
   - UAT: `http://localhost:5001` (API), `localhost:5433` (DB)
   - Prod: `http://localhost:5002` (API), `localhost:5434` (DB)
   - Connexion DB: `psql -h localhost -p 5433 -U uat_user -d uat_fintech`
8. **Blue/Green deployment**: Concept, swap, benefits
9. **Rollback et récupération**:
   - Stratégies selon MODE
   - Commandes pratiques
   - Blue/Green instant rollback
10. **Monitoring et logs**: `docker-compose logs -f`, healthcheck
11. **Sécurité**: Secrets GitHub, variables sensibles
12. **Troubleshooting**: Port conflicts, healthcheck fails, DB connection issues
13. **Migration de données**: Gestion des migrations entre déploiements
14. **Checklist pré-déploiement**: Vérifications avant push tag

## 🔐 Sécurité et Secrets

**Secrets GitHub requis:**
- **`DOCKERHUB_USERNAME`**: Username Docker Hub (si MODE=image)
- **`DOCKERHUB_TOKEN`**: Token Docker Hub (si push image)
- **`PROD_SECRET_KEY`**: Flask SECRET_KEY pour production (cryptographiquement sûr)
- **`PROD_DB_PASSWORD`**: Mot de passe PostgreSQL production
- **`UAT_DB_PASSWORD`**: Mot de passe PostgreSQL UAT (optionnel, peut être hardcodé en dev)

**Variables d'environnement (docker-compose):**

```yaml
# CI (docker-compose.ci.yml)
DATABASE_URL: sqlite:///instance/transactions.db
FLASK_ENV: development
SECRET_KEY: dev-secret-key-not-for-production

# UAT (docker-compose.uat.yml)
DATABASE_URL: postgresql://uat_user:${UAT_DB_PASSWORD}@db:5432/uat_fintech
FLASK_ENV: development
SECRET_KEY: uat-secret-key-change-me

# Prod (docker-compose.prod-blue/green.yml)
DATABASE_URL: postgresql://prod_user:${PROD_DB_PASSWORD}@db:5432/prod_fintech
FLASK_ENV: production
SECRET_KEY: ${PROD_SECRET_KEY}
```

**Bonnes pratiques:**
- Ne jamais commit de secrets dans le code
- Utiliser GitHub Secrets pour valeurs sensibles
- Rotation régulière des passwords
- SECRET_KEY Flask: minimum 32 caractères random (`secrets.token_hex(32)`)

## 🐳 Configuration Docker

**Dockerfile (app_bank/Dockerfile):**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . ./app_bank/

# Create instance directory for SQLite (CI/dev)
RUN mkdir -p instance

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app_bank/app.py"]
```

**Docker Compose CI (docker/docker-compose.ci.yml):**

```yaml
services:
  web:
    build:
      context: ..
      dockerfile: app_bank/Dockerfile
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: sqlite:///instance/transactions.db
      FLASK_ENV: development
      SECRET_KEY: ci-test-secret-key
    volumes:
      - ../app_bank/instance:/app/instance
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
```

**Docker Compose UAT (docker/docker-compose.uat.yml):**

```yaml
services:
  web:
    build:
      context: ..
      dockerfile: app_bank/Dockerfile
    ports:
      - "5001:5000"
    environment:
      DATABASE_URL: postgresql://uat_user:uat_password@db:5432/uat_fintech
      FLASK_ENV: development
      SECRET_KEY: uat-secret-key-change-me
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 10s
      timeout: 5s
      retries: 5
  
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: uat_user
      POSTGRES_PASSWORD: uat_password
      POSTGRES_DB: uat_fintech
    ports:
      - "5433:5432"
    volumes:
      - uat_db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U uat_user"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  uat_db_data:
```

**Docker Compose Prod Blue (docker/docker-compose.prod-blue.yml):**

```yaml
services:
  web-blue:
    build:
      context: ..
      dockerfile: app_bank/Dockerfile
    ports:
      - "5002:5000"
    environment:
      DATABASE_URL: postgresql://prod_user:${PROD_DB_PASSWORD}@db-blue:5432/prod_fintech
      FLASK_ENV: production
      SECRET_KEY: ${PROD_SECRET_KEY}
    depends_on:
      db-blue:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 10s
      timeout: 5s
      retries: 5
    profiles:
      - blue
  
  db-blue:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: prod_user
      POSTGRES_PASSWORD: ${PROD_DB_PASSWORD}
      POSTGRES_DB: prod_fintech
    ports:
      - "5434:5432"
    volumes:
      - prod_blue_db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U prod_user"]
      interval: 10s
      timeout: 5s
      retries: 5
    profiles:
      - blue

volumes:
  prod_blue_db_data:
```

**Docker Compose Prod Green (similaire avec `-green` suffix et profile `green`)

## ✅ Checklist de génération complète

Génère le projet Fintech avec:

### Structure et Code
- [x] Structure de fichiers: `app_bank/`, `docker/`, `k6/`, `tests/`, `.github/workflows/`, `docs/`
- [x] **app.py**: Flask factory, SQLite WAL config, Postgres migration password_hash VARCHAR(255)
- [x] **models.py**: User et Transaction avec relations SQLAlchemy
- [x] **extensions.py**: db, login_manager, bcrypt instances
- [x] **requirements.txt**: Flask, SQLAlchemy, Flask-Login, psycopg2-binary, bcrypt, pytest, etc.
- [x] **routes/auth.py**: register, login, logout avec Flask-Login
- [x] **routes/transactions.py**: create, list transactions
- [x] **routes/health.py**: healthcheck endpoint (status + version)
- [x] **routes/main.py**: /, dashboard, accounting, trading
- [x] **templates/**: base.html, login.html, register.html, dashboard.html, etc.
- [x] **static/css/**: login.css, dashboard.css

### Tests
- [x] **tests/test_auth.py**: Tests register, login, logout, password validation
- [x] **tests/test_transactions.py**: Tests create, list, validation montants
- [x] **tests/test_health.py**: Test GET /health
- [x] **tests/conftest.py**: Fixtures app, client, db avec config test
- [x] Couverture > 70%

### Performance k6
- [x] **k6/perf-smoke.js**: 1 VU, 10s, GET /health, seuils p95<500ms
- [x] **k6/perf-load.js**: 0→40 VUs, register once per VU, login→dashboard, WAL-friendly
- [x] Seuils adaptés: p95<800ms, errors<10-20%

### Docker
- [x] **Dockerfile**: Python 3.11-slim, curl, healthcheck
- [x] **docker-compose.ci.yml**: SQLite, port 5000
- [x] **docker-compose.uat.yml**: Postgres, ports 5001/5433
- [x] **docker-compose.prod-blue.yml**: Postgres, ports 5002/5434, profiles
- [x] **docker-compose.prod-green.yml**: Idem avec suffix -green
- [x] Healthchecks sur tous les services
- [x] Pas de clé "version" (deprecated)

### CI/CD Workflows
- [x] **.github/workflows/ci.yml**: 
  - Triggers: push main, PR main
  - 17 étapes: checkout → build → test → scans → k6 → artifacts
  - k6 avec -u 0:0 pour permissions summary
  - k6 load toujours exécuté
  - Upload 7 artifacts
- [x] **.github/workflows/cd-local.yml**:
  - Triggers: push main (UAT auto), push tags v* (Prod gated)
  - Variables via $GITHUB_ENV (pas inputs.* sur push)
  - MODE=build par défaut
  - Approval gate pour Prod
  - Healthcheck + smoke post-deploy

### Sécurité
- [x] pip-audit pour SCA (audit.json)
- [x] Bandit pour SAST (bandit.json)
- [x] Trivy pour container scan (trivy.sarif → GitHub Security)
- [x] OWASP ZAP pour DAST (zap-report.html)
- [x] GitHub Secrets: PROD_SECRET_KEY, PROD_DB_PASSWORD, DOCKERHUB_*
- [x] Pas de secrets hardcodés

### Base de données
- [x] SQLite pour CI/dev (instance/transactions.db)
- [x] PostgreSQL 16 Alpine pour UAT/Prod
- [x] SQLite WAL mode + busy_timeout 5000ms
- [x] Migration auto password_hash VARCHAR(255) pour Postgres
- [x] Volumes Docker persistants (uat_db_data, prod_blue_db_data)

### Documentation
- [x] **docs/CI-PIPELINE.md**: 
  - Vue d'ensemble, prérequis, architecture
  - 17 étapes détaillées avec commandes
  - Description artifacts
  - SQLite optimizations
  - Troubleshooting
  - Section 13: Comparaison k6 smoke vs load
- [x] **docs/CD-PIPELINE.md**:
  - Déclencheurs (main UAT, v* Prod)
  - Environnements UAT vs Prod
  - MODE=image vs MODE=build
  - Accès: localhost:5001 (UAT), localhost:5002 (Prod)
  - Blue/Green strategy
  - Rollback procedures
  - Troubleshooting
- [x] Documentation complète en français

### Autres
- [x] **.gitignore**: Python (__pycache__, *.pyc, venv), Docker, SQLite, IDE (.vscode, .idea)
- [x] **README.md**: Description projet, quick start, architecture
- [x] **create_users.py**: Script création utilisateurs de test
- [x] Migration de schéma compatible SQLite ↔ Postgres

## 🎯 Résultat attendu

Un projet **Fintech-test** production-ready avec:
- ✅ Application Flask complète: auth, transactions, dashboard
- ✅ Pipeline CI de 17 étapes avec 4 scans sécurité + 2 tests k6
- ✅ Pipeline CD Blue/Green: UAT auto + Prod gated
- ✅ Base de données: SQLite (CI) + PostgreSQL (UAT/Prod) avec migration auto
- ✅ Tests de performance k6: smoke (validation rapide) + load (charge réaliste 40 VUs)
- ✅ Sécurité: pip-audit, Bandit, Trivy SARIF, OWASP ZAP
- ✅ Documentation française complète (CI-PIPELINE.md + CD-PIPELINE.md)
- ✅ Docker multi-environnements (ci, uat, prod-blue, prod-green)
- ✅ Artifacts CI: 7 fichiers (coverage, scans, k6 summaries, ZAP report)
- ✅ Rollback strategies: image pull, git revert, Blue/Green swap
- ✅ Ports: 5000 (CI), 5001 (UAT API), 5002 (Prod API), 5433 (UAT DB), 5434 (Prod DB)
- ✅ Self-hosted runner ready (WSL2 Ubuntu)
- ✅ GitHub Security integration (Trivy SARIF)
- ✅ Healthchecks partout (app + databases)
- ✅ Architecture scalable et maintenable

**Commandes de démarrage rapide:**

```bash
# Clone et setup
git clone <repo-url> fintech-test
cd fintech-test

# CI local test
docker-compose -f docker/docker-compose.ci.yml up --build

# UAT local deploy
docker-compose -f docker/docker-compose.uat.yml up -d

# Prod deploy (après setup runner)
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin v1.0.0
# Approuver dans GitHub → Déploiement auto

# Accès
# CI: http://localhost:5000
# UAT: http://localhost:5001
# Prod: http://localhost:5002
```

---

**🎉 Voilà ! Copier tout ce qui est sous "PROMPT COMPLET - PROJET FINTECH" dans VS Code Copilot pour recréer le projet exact avec toute l'architecture CI/CD.**
