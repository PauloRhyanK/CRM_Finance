# app/main/routes/interaction_routes.py

from flask import Blueprint, request, jsonify
from app.services import interaction_service
from app.schemas.interaction_schema import InteractionSchema

interaction_bp = Blueprint('interaction', __name__)
interaction_schema = InteractionSchema()
interactions_schema = InteractionSchema(many=True)

@interaction_bp.route('/api/customers/<customer_id>/interactions', methods=['POST'])
def create_interaction(customer_id):
    """Cria um novo registro de interação para um cliente específico."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
    
    # Garante que a interação está a ser criada para o cliente correto
    data['cd_customer'] = customer_id
    
    # TODO: Idealmente, o cd_user viria de um token de autenticação do usuário logado
    # Por agora, vamos assumir que ele é passado no corpo da requisição.
    if 'cd_user' not in data:
         return jsonify({'error': 'cd_user é obrigatório'}), 400

    new_interaction = interaction_service.create_interaction(data)
    
    return jsonify({
        'message': 'Interação registrada com sucesso',
        'interaction': interaction_schema.dump(new_interaction)
    }), 201

@interaction_bp.route('/api/customers/<customer_id>/interactions', methods=['GET'])
def get_interactions(customer_id):
    """Lista todas as interações de um cliente específico com paginação."""
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 15, type=int), 100)
    
    paginated_interactions = interaction_service.get_interactions_for_customer(
        customer_id, page=page, per_page=per_page
    )
    
    return jsonify({
        'interactions': interactions_schema.dump(paginated_interactions.items),
        'total': paginated_interactions.total,
        'pages': paginated_interactions.pages,
        'current_page': page
    }), 200