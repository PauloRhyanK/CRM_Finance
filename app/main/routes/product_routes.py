# app/main/routes/product_routes.py

from flask import Blueprint, request, jsonify
from app.services import product_service
from app.schemas.product_schema import ProductSchema

# --- Configuração do Blueprint e Esquemas ---
product_bp = Blueprint('product', __name__, url_prefix='/api/products')
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# --- ROTAS (ENDPOINTS) ---

@product_bp.route('', methods=['POST'])
def create_product():
    """Cria um novo produto ou serviço."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
    
    # O serviço levanta uma exceção (InvalidDataError) se os dados forem ruins.
    # O tratador de erros global em __init__.py irá capturar e formatar a resposta.
    new_product = product_service.create_product(data)
    
    return jsonify({
        'message': 'Produto criado com sucesso',
        'product': product_schema.dump(new_product)
    }), 201

@product_bp.route('', methods=['GET'])
def get_products():
    """Lista todos os produtos com paginação."""
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 20, type=int), 100)
    
    paginated_products = product_service.get_all_products(page=page, per_page=per_page)
    
    return jsonify({
        'products': products_schema.dump(paginated_products.items),
        'total': paginated_products.total,
        'pages': paginated_products.pages,
        'current_page': page
    }), 200

@product_bp.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    """Busca um produto específico pelo seu ID."""
    # O serviço levanta ProductNotFoundError, que o tratador global converte para 404.
    product = product_service.get_product_by_id(product_id)
    return jsonify({'product': product_schema.dump(product)}), 200

@product_bp.route('/<product_id>', methods=['PUT'])
def update_product(product_id):
    """Atualiza os dados de um produto existente."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
        
    updated_product = product_service.update_product(product_id, data)
    
    return jsonify({
        'message': 'Produto atualizado com sucesso',
        'product': product_schema.dump(updated_product)
    }), 200

@product_bp.route('/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Desativa (soft delete) ou remove permanentemente um produto."""
    hard_delete = request.args.get('hard_delete', 'false').lower() == 'true'
    product_service.delete_product(product_id, soft_delete=not hard_delete)
    
    message = "Produto removido permanentemente" if hard_delete else "Produto desativado com sucesso"
    return jsonify({'message': message}), 200