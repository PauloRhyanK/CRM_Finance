# app/main/routes/auth_routes.py
from flask import Blueprint, request, jsonify
from app.services import auth_service
from app.util.exceptions import ServiceError # Apenas para o tratador de erro saber que existe

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado enviado"}), 400

    # O serviço levanta uma exceção se der erro, que é capturada pelo tratador global.
    user = auth_service.register_new_user(form_data=data)
    
    # Se chegarmos aqui, foi um sucesso.
    return jsonify({"message": "Usuário registrado com sucesso!"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado enviado"}), 400

    # O serviço levanta AuthenticationError se as credenciais estiverem erradas.
    user = auth_service.authenticate_user(form_data=data)
    
    # TODO: Implementar a geração de um token JWT (JSON Web Token) aqui.
    return jsonify({
        "message": "Login bem-sucedido.",
        "user": {
            "username": user.ds_user,
            "email": user.ds_user_email
        },
        # "token": jwt_token  <-- Adicionar quando implementar JWT
    }), 200