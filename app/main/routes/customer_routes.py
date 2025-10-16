from flask import Blueprint, request, jsonify
from app.services import customer_service
import uuid

customer_bp = Blueprint('customer', __name__, url_prefix='/api/customers')

@customer_bp.route('', methods=['POST'])

def create_customer():
    """
    Cria um novo cliente.
    
    Body (JSON):
    {
        "ds_customer_name": "Nome do Cliente",
        "ds_customer_email": "email@exemplo.com",
        "ds_customer_phone": "(11) 99999-9999",
        "ds_customer_cpf_cnpj": "123.456.789-00",
        "ds_customer_address": "Rua Exemplo, 123",
        "ds_customer_city": "São Paulo",
        "ds_customer_state": "SP",
        "ds_customer_zip_code": "01234-567",
        "ds_customer_country": "Brasil"
    }
    """
    try:
        # Obter dados JSON da requisição com tratamento de encoding
        data = request.get_json()
        
        if not data:
            return {'error': 'Dados não fornecidos'}, 400
        customer, message = customer_service.create_customer(data)
        
        if customer:
            
            return {
                'message': message,
                'customer': customer.to_dict()
            }, 201
        else:
            return {'error': message}, 400
            
    except Exception as e:
        return {'error': f'Erro interno: {str(e)}'}, 500

@customer_bp.route('', methods=['GET'])
def get_customers():
    """
    Lista clientes com paginação e filtros.
    
    Query parameters:
    - page: número da página (default: 1)
    - per_page: itens por página (default: 20)
    - active_only: apenas ativos (default: true)
    - search: termo de busca
    """
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        active_only = request.args.get('active_only', 'true').lower() == 'true'
        search_term = request.args.get('search')
        
        # Limitar per_page para evitar sobrecarga
        per_page = min(per_page, 100)
        
        if search_term:
            # Se há termo de busca, usar função de pesquisa
            customers = customer_service.search_customers(search_term, active_only=active_only)
            return {
                'customers': customers,
                'total': len(customers),
                'search_term': search_term
            }, 200
        else:
            # Lista paginada normal
            result = customer_service.get_all_customers(
                active_only=active_only,
                page=page,
                per_page=per_page
            )
            
            return result, 200
            
    except Exception as e:
        return {'error': f'Erro interno: {str(e)}'}, 500

@customer_bp.route('/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    """
    Busca um cliente específico pelo ID.
    """
    try:
        # Validar formato UUID
        try:
            uuid.UUID(customer_id)
        except ValueError:
            return jsonify({'error': 'ID de cliente inválido'}), 400
        
        customer, message = customer_service.get_customer_by_id(customer_id)
        
        if customer:
            return jsonify({
                'customer': customer.to_dict()
            }), 200
        else:
            return jsonify({'error': message}), 404
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@customer_bp.route('/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """
    Atualiza os dados de um cliente.
    """
    try:
        # Validar formato UUID
        try:
            uuid.UUID(customer_id)
        except ValueError:
            return {'error': 'ID de cliente inválido'}, 400
        
        # Usa dados processados pelo middleware
        data = request.get_json()
        
        if not data:
            return {'error': 'Dados não fornecidos'}, 400
        
        customer, message = customer_service.update_customer(customer_id, data)
        
        if customer:
            return {
                'message': message,
                'customer': customer.to_dict()
            }, 200
        else:
            return jsonify({'error': message}), 400
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@customer_bp.route('/<customer_id>', methods=['DELETE'])

def delete_customer(customer_id):
    """
    Remove um cliente (soft delete por padrão).
    
    Query parameters:
    - hard_delete: true para remoção permanente (default: false)
    """
    try:
        # Validar formato UUID
        try:
            uuid.UUID(customer_id)
        except ValueError:
            return jsonify({'error': 'ID de cliente inválido'}), 400
        
        hard_delete = request.args.get('hard_delete', 'false').lower() == 'true'
        soft_delete = not hard_delete
        
        success, message = customer_service.delete_customer(customer_id, soft_delete=soft_delete)
        
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'error': message}), 400
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@customer_bp.route('/<customer_id>/activate', methods=['PATCH'])

def activate_customer(customer_id):
    """
    Reativa um cliente desativado.
    """
    try:
        # Validar formato UUID
        try:
            uuid.UUID(customer_id)
        except ValueError:
            return jsonify({'error': 'ID de cliente inválido'}), 400
        
        success, message = customer_service.activate_customer(customer_id)
        
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'error': message}), 400
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@customer_bp.route('/search', methods=['GET'])

def search_customers():
    """
    Endpoint dedicado para busca de clientes.
    
    Query parameters:
    - q: termo de pesquisa (obrigatório)
    - fields: campos para buscar (name,email,cpf_cnpj)
    - active_only: apenas ativos (default: true)
    """
    try:
        search_term = request.args.get('q')
        
        if not search_term:
            return jsonify({'error': 'Termo de pesquisa obrigatório'}), 400
        
        fields_param = request.args.get('fields', 'name,email,cpf_cnpj')
        search_fields = [field.strip() for field in fields_param.split(',') if field.strip()]
        
        # Validar campos
        valid_fields = ['name', 'email', 'cpf_cnpj']
        search_fields = [field for field in search_fields if field in valid_fields]
        
        if not search_fields:
            search_fields = ['name', 'email', 'cpf_cnpj']
        
        active_only = request.args.get('active_only', 'true').lower() == 'true'
        
        customers = customer_service.search_customers(
            search_term=search_term,
            search_fields=search_fields,
            active_only=active_only
        )
        
        return jsonify({
            'customers': customers,
            'total': len(customers),
            'search_term': search_term,
            'search_fields': search_fields
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

# Handlers de erro específicos
@customer_bp.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Recurso não encontrado'}), 404

@customer_bp.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({'error': 'Método não permitido'}), 405

@customer_bp.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Erro interno do servidor'}), 500