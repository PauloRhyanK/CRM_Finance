# app/services/customer_service.py

from app import db
from app.models.customer_model import Customer
from app.schemas.customer_schema import CustomerSchema
from app.util.exceptions import CustomerNotFoundError, InvalidDataError
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True) # Esquema para listas de clientes

def create_customer(customer_data):
    """Cria um novo cliente. Levanta exceções em caso de erro."""
    try:
        customer = customer_schema.load(customer_data, session=db.session)

        if not customer.validate_cpf_cnpj():
            raise InvalidDataError("CPF/CNPJ em formato inválido")

        db.session.add(customer)
        db.session.commit()
        return customer
    except ValidationError as err:
        raise InvalidDataError(err.messages)
    except IntegrityError:
        db.session.rollback()
        # Idealmente, a rota trataria a mensagem específica (Email/CPF)
        raise InvalidDataError("Email ou CPF/CNPJ já está em uso.")

def get_customer_by_id(customer_id):
    """Busca um cliente pelo ID. Levanta CustomerNotFoundError se não encontrar."""
    customer = Customer.query.filter_by(cd_customer=customer_id).first()
    if not customer:
        raise CustomerNotFoundError()
    return customer

def update_customer(customer_id, customer_data):
    """Atualiza um cliente. Levanta CustomerNotFoundError ou InvalidDataError."""
    customer = get_customer_by_id(customer_id) # Reutiliza a função de busca

    try:
        # O 'partial=True' permite atualizações parciais
        updated_customer = customer_schema.load(
            customer_data, instance=customer, partial=True, session=db.session
        )

        if 'ds_customer_cpf_cnpj' in customer_data and not updated_customer.validate_cpf_cnpj():
            raise InvalidDataError("CPF/CNPJ em formato inválido")
        
        db.session.commit()
        return updated_customer
    except ValidationError as err:
        raise InvalidDataError(err.messages)
    except IntegrityError:
        db.session.rollback()
        raise InvalidDataError("Email ou CPF/CNPJ já está em uso por outro cliente.")

def delete_customer(customer_id, soft_delete=True):
    """Remove um cliente (soft ou hard delete)."""
    customer = get_customer_by_id(customer_id)
    
    if soft_delete:
        customer.is_customer_active = False
    else:
        db.session.delete(customer)
    
    db.session.commit()
    # Para delete, podemos não retornar nada ou uma mensagem de sucesso
    return True

# Funções de listagem e busca geralmente não levantam exceções,
# apenas retornam listas (vazias ou não) ou dicionários. Seu código para elas já está bom!
# ... (get_all_customers, search_customers, activate_customer continuam como estão) ...