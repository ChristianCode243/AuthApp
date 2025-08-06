from flask import Flask, request, jsonify
from flask_jwt_extended import (
    create_access_token, jwt_required,
    get_jwt_identity, set_access_cookies, unset_jwt_cookies
)
from datetime import timedelta

from extensions import db, bcrypt, jwt, cors
from models import User

def create_app():
    app = Flask(__name__)
    
    # --- CONFIGURATIONS ---
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['JWT_SECRET_KEY'] = 'secret'
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token_cookie'
    app.config['JWT_COOKIE_SECURE'] = False  # True si HTTPS
    app.config['JWT_COOKIE_SAMESITE'] = 'Lax'  # ou 'None' si HTTPS + front différent
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # True si tu veux plus de sécurité

    # --- INITIALISATION DES EXTENSIONS ---
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, supports_credentials=True, origins=["http://localhost:3000"])

    with app.app_context():
        db.create_all()

    # --- ROUTES ---
    @app.route('/')
    def index():
        return jsonify({"msg": "Bienvenue dans l'application OAuth!"})

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({"msg": "Champs manquants"}), 400

        if User.query.filter_by(email=data['email']).first():
            return jsonify({"msg": "Email déjà utilisé"}), 400

        hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(email=data['email'], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "Utilisateur créé"}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()

        if not data or not data.get('email') or not data.get('password'):
            return jsonify({"msg": "Champs manquants"}), 400

        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not bcrypt.check_password_hash(user.password, data['password']):
            return jsonify({"msg": "Identifiants invalides"}), 401

        # Crée un JWT pour l'utilisateur (en utilisant l'email comme identité par ex.)
        access_token = create_access_token(
            identity=user.email,  # ou user.id, mais dans /me tu dois le récupérer proprement
            expires_delta=timedelta(days=1)
        )

        # Crée la réponse
        response = jsonify({
            "msg": "Connecté",
            "email": user.email  # utile pour retour immédiat côté frontend
        })

        # Ajoute le JWT dans les cookies
        set_access_cookies(response, access_token)

        return response, 200

    @app.route('/logout', methods=['POST'])
    def logout():
        resp = jsonify({"msg": "Déconnecté"})
        unset_jwt_cookies(resp)
        return resp

    # @app.route('/me', methods=['GET'])
    # @jwt_required()
    # def me():
    #     user_id = get_jwt_identity()
    #     user = User.query.get(user_id)
    #     if user:
    #         return jsonify({
    #             "userId": user_id,
    #             "email": user.email
    #         })
    #     return jsonify({"msg": "Utilisateur non trouvé"}), 404
    
    @app.route('/me', methods=['GET'])
    @jwt_required()
    def me():
        identity = get_jwt_identity()
        return jsonify({"email": identity})

    @app.route('/hello', methods=['GET'])
    @jwt_required()
    def helloWorld():
        return jsonify({"msg": "Hello world!"})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
