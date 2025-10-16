# app/main/routes/customer_routes.py
from flask import Blueprint, request, jsonify
from app.services import customer_service
from app.schemas.customer_schema import CustomerSchema
# from app.util.decorators import validate_uuid # Supondo que você criou o decorador

customer_bp = Blueprint('customer', __name__, url_prefix='/api/customers')
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@customer_bp.route('', methods=['POST'])
def create_customer():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
    
    # O serviço agora levanta exceções de validação ou integridade.
    new_customer = customer_service.create_customer(data)
    
    return jsonify({
        'message': 'Cliente criado com sucesso',
        'customer': customer_schema.dump(new_customer) # Usando o schema para a saída
    }), 201

@customer_bp.route('/<customer_id>', methods=['GET'])
# @validate_uuid('customer_id') # Adicione o decorador para validar o UUID!
def get_customer(customer_id):
    customer = customer_service.get_customer_by_id(customer_id)
    return jsonify({'customer': customer_schema.dump(customer)}), 200

@customer_bp.route('/<customer_id>', methods=['PUT'])
# @validate_uuid('customer_id')
def update_customer(customer_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados não fornecidos'}), 400
        
    updated_customer = customer_service.update_customer(customer_id, data)
    
    return jsonify({
        'message': 'Cliente atualizado com sucesso',
        'customer': customer_schema.dump(updated_customer)
    }), 200

@customer_bp.route('/<customer_id>', methods=['DELETE'])
# @validate_uuid('customer_id')
def delete_customer(customer_id):
    hard_delete = request.args.get('hard_delete', 'false').lower() == 'true'
    customer_service.delete_customer(customer_id, soft_delete=not hard_delete)
    
    message = "Cliente removido permanentemente" if hard_delete else "Cliente desativado com sucesso"
    return jsonify({'message': message}), 200

# ... (as outras rotas como `get_customers` e `search` podem ser refatoradas de forma similar) ...