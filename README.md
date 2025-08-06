# 🔐 AuthApp — Authentification sécurisée Fullstack (Next.js + Flask + SQLite + Docker)

> **AuthApp** est une application web d’authentification fullstack développée avec **Next.js** (frontend) et **Flask** (backend). Elle utilise **JWT stocké en cookie sécurisé**, avec **SQLite** comme base de données locale, le tout conteneurisé avec **Docker** et **servi par Nginx**.


## ✨ Fonctionnalités

* 🔐 Authentification sécurisée avec **JWT** (dans `HttpOnly Cookie`)
* 📦 API RESTful construite avec **Flask**
* 💻 Interface utilisateur moderne avec **Next.js**
* 🗄️ Base de données **SQLite3** (simple, locale, portable)
* 🔁 **Nginx** comme reverse proxy (frontend + backend)
* 🐳 Déploiement local avec **Docker** via `docker-compose`
* 🧠 Structure claire, scalable et prête à être déployée en production


## 🧱 Stack Technique

| Côté            | Technologies                                |
| --------------- | ------------------------------------------- |
| Frontend        | Next.js, React, TailwindCSS                 |
| Backend         | Flask, Flask-JWT-Extended, Flask-SQLAlchemy |
| Base de données | SQLite (fichier local `database.db`)        |
| Auth            | JWT (via cookie sécurisé `HttpOnly`)        |
| DevOps          | Docker, Docker Compose, Nginx               |


## 📁 Structure du projet

```
authapp/
│
├── backend/              # API Flask + JWT
│   ├── app.py
│   ├── models.py
│   ├── auth.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/             # Frontend Next.js
│   ├── app/
│   ├── pages/
│   ├── components/
│   ├── lib/api.ts
│   └── ...
│
├── nginx/
│   └── default.conf      # Configuration du reverse proxy
│
├── docker-compose.yml    # Orchestration
├── .env                  # Variables d’environnement
└── README.md             # Ce fichier
```


## 🚀 Installation & Exécution locale

### Prérequis

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)


### Étapes

1. **Clone le dépôt**

```bash
git clone https://github.com/votre-utilisateur/authapp.git
cd authapp
```

2. **Lancer les services Docker**

```bash
docker-compose up --build
```

3. **Accéder à l'application**

| Service     | URL                                          |
| ----------- | -------------------------------------------- |
| Frontend    | [http://localhost](http://localhost)         |
| Backend API | [http://localhost/api](http://localhost/api) |


## 🔐 Authentification — Comment ça marche ?

* Lors du **login**, le serveur Flask :

  * Vérifie les identifiants
  * Génére un **JWT**
  * Envoie le JWT dans un cookie sécurisé `HttpOnly`
* Le **frontend** stocke rien côté JS (sécurité renforcée)
* Le token est automatiquement inclus dans les requêtes par le navigateur
* `/me` permet de récupérer l’utilisateur authentifié


## ⚙️ Configuration Docker

### `docker-compose.yml`

* 3 services :

  * `frontend` : Next.js app
  * `backend` : Flask app
  * `nginx` : reverse proxy
* Le volume `sqlite_data` permet la **persistance du fichier SQLite**


## 🧪 Endpoints de l'API (Flask)

| Méthode | URL       | Description                     |
| ------- | --------- | ------------------------------- |
| POST    | `/login`  | Connexion (retourne un JWT)     |
| GET     | `/me`     | Retourne l’utilisateur connecté |
| GET     | `/logout` | Déconnexion (efface le cookie)  |

---

## 🔐 Exemple de requêtes

```ts
// Login depuis Next.js
await api.post('/login', { email, password })

// Récupérer l'utilisateur connecté
const res = await api.get('/me')
```


## ✅ À venir (Roadmap)

* [ ] Intégration PostgreSQL (optionnel)
* [ ] Middleware de protection des routes côté frontend
* [ ] Enregistrement (signup) d’un nouvel utilisateur
* [ ] Tests automatisés (frontend & backend)
* [ ] Déploiement sur Railway / Vercel


## 📸 Screenshots

> <img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/3ad62b43-b185-4586-96e4-8aa4ea552e49" />



## 📚 Ressources utiles

* [Flask-JWT-Extended Docs](https://flask-jwt-extended.readthedocs.io/)
* [Next.js](https://nextjs.org/)
* [SQLite](https://www.sqlite.org/index.html)
* [Docker](https://docs.docker.com/)
* [Nginx](https://nginx.org/)


## 👨‍💻 Auteur

**Christian Mandika**
Développeur Fullstack | Passionné par l’automatisation, les solutions simples, et la création de produits utiles.
📫 *\[LinkedIn / Portfolio / GitHub à insérer ici]*


## 📝 Licence

Ce projet est open-source sous licence MIT.
