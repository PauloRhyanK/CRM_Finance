# Arquivo: app/routes/auth_routes.py

from flask import Blueprint, request, jsonify
from app.services import auth_service

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Endpoint para registrar um novo usuário.
    Espera um JSON com os dados do usuário no corpo da requisição.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado enviado"}), 400

    user, message = auth_service.register_new_user(form_data=data)

    if user:
        return jsonify({"message": message}), 201
    else:
        return jsonify({"error": message}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint para autenticar um usuário.
    Espera um JSON com 'ds_user_email' e 'password'.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado enviado"}), 400

    user, message = auth_service.authenticate_user(form_data=data)

    if user:
        return jsonify({
            "message": message,
            "user": {
                "username": user.ds_user,
                "email": user.ds_user_email
            }
        }), 200
    else:
        return jsonify({"error": message}), 401