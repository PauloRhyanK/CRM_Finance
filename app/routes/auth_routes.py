# Arquivo: app/routes/auth_routes.py

from flask import Blueprint, request, jsonify
from app.services import auth_service

# Criamos um "Blueprint", que é como um mini-aplicativo para organizar
# um conjunto de rotas relacionadas. Todas as rotas aqui terão o prefixo /auth.
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Endpoint para registrar um novo usuário.
    Espera um JSON com os dados do usuário no corpo da requisição.
    """
    # 1. Pega o dicionário JSON enviado na requisição. É aqui que nasce o 'form_data'!
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado enviado"}), 400

    # 2. Chama o serviço para fazer a lógica de registro, passando os dados
    user, message = auth_service.register_new_user(form_data=data)

    # 3. Retorna uma resposta baseada no resultado do serviço
    if user:
        # 201 Created: Código HTTP para quando um recurso é criado com sucesso
        return jsonify({"message": message}), 201
    else:
        # 400 Bad Request: O cliente enviou algo errado (ex: email já existe)
        return jsonify({"error": message}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint para autenticar um usuário.
    Espera um JSON com 'ds_user_email' e 'password'.
    """
    # 1. Pega os dados da requisição
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado enviado"}), 400

    # 2. Chama o serviço para fazer a lógica de autenticação
    user, message = auth_service.authenticate_user(form_data=data)

    # 3. Retorna uma resposta baseada no resultado
    if user:
        # No futuro, aqui nós geraríamos e retornaríamos um token de acesso (JWT)
        # Por agora, apenas confirmamos o sucesso.
        # 200 OK: Código HTTP para sucesso
        return jsonify({
            "message": message,
            "user": {
                "username": user.ds_user,
                "email": user.ds_user_email
            }
        }), 200
    else:
        # 401 Unauthorized: Código HTTP para falha na autenticação
        return jsonify({"error": message}), 401