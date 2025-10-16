# app/main/routes/customer_routes.py

from flask import Blueprint, request, jsonify
from app.services import customer_service
from app.schemas.customer_schema import CustomerSchema
from app.util.decorators import validate_uuid # Importando nosso novo decorador

customer_bp = Blueprint('customer', __name__, url_prefix='/api/customers')
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@customer_bp.route('', methods=['POST'])
def create_customer():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
    
    new_customer = customer_service.create_customer(data)
    
    return jsonify({
        'message': 'Cliente criado com sucesso',
        'customer': customer_schema.dump(new_customer)
    }), 201

@customer_bp.route('', methods=['GET'])
def get_customers():
    """
    Lista clientes com paginação e busca.
    Query params: page, per_page, active_only, search
    """
    args = {
        'page': request.args.get('page', 1, type=int),
        'per_page': min(request.args.get('per_page', 20, type=int), 100),
        'active_only': request.args.get('active_only', 'true').lower() == 'true',
        'search_term': request.args.get('search')
    }
    
    paginated_customers = customer_service.get_customers_list(args)
    
    return jsonify({
        'customers': customers_schema.dump(paginated_customers.items),
        'total': paginated_customers.total,
        'pages': paginated_customers.pages,
        'current_page': paginated_customers.page
    }), 200

@customer_bp.route('/<string:customer_id>', methods=['GET'])
@validate_uuid('customer_id') # Aplicando o decorador!
def get_customer(customer_id):
    customer = customer_service.get_customer_by_id(customer_id)
    return jsonify({'customer': customer_schema.dump(customer)}), 200

@customer_bp.route('/<string:customer_id>', methods=['PUT'])
@validate_uuid('customer_id') # Aplicando o decorador!
def update_customer(customer_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
        
    updated_customer = customer_service.update_customer(customer_id, data)
    
    return jsonify({
        'message': 'Cliente atualizado com sucesso',
        'customer': customer_schema.dump(updated_customer)
    }), 200

@customer_bp.route('/<string:customer_id>', methods=['DELETE'])
@validate_uuid('customer_id') # Aplicando o decorador!
def delete_customer(customer_id):
    hard_delete = request.args.get('hard_delete', 'false').lower() == 'true'
    customer_service.delete_customer(customer_id, soft_delete=not hard_delete)
    
    message = "Cliente removido permanentemente" if hard_delete else "Cliente desativado com sucesso"
    return jsonify({'message': message}), 200

@customer_bp.route('/<string:customer_id>/activate', methods=['PATCH'])
@validate_uuid('customer_id') # Aplicando o decorador!
def activate_customer(customer_id):
    # O serviço activate_customer precisa ser refatorado para usar exceções também.
    # Supondo que isso foi feito:
    customer_service.activate_customer(customer_id)
    return jsonify({'message': 'Cliente reativado com sucesso'}), 200