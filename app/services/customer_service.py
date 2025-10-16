from app import db
from app.models.customer_model import Customer
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import uuid

def create_customer(customer_data):
    """
    Cria um novo cliente no banco de dados.
    
    Args:
        customer_data (dict): Dados do cliente
        
    Returns:
        tuple: (Customer object or None, message)
    """
    try:
        # Validação básica dos campos obrigatórios
        required_fields = ['ds_customer_name', 'ds_customer_email']
        for field in required_fields:
            if not customer_data.get(field):
                return None, f"Campo obrigatório ausente: {field}"
        # Criar novo cliente
        customer = Customer(
            ds_customer_name=customer_data['ds_customer_name'],
            ds_customer_email=customer_data['ds_customer_email'],
            ds_customer_phone=customer_data.get('ds_customer_phone'),
            ds_customer_cpf_cnpj=customer_data.get('ds_customer_cpf_cnpj'),
            ds_customer_address=customer_data.get('ds_customer_address'),
            ds_customer_city=customer_data.get('ds_customer_city'),
            ds_customer_state=customer_data.get('ds_customer_state'),
            ds_customer_zip_code=customer_data.get('ds_customer_zip_code'),
            ds_customer_country=customer_data.get('ds_customer_country', 'Brasil')
        )
        
        # Validar CPF/CNPJ se fornecido
        if not customer.validate_cpf_cnpj():
            return None, "CPF/CNPJ em formato inválido"

        db.session.add(customer)
        db.session.commit()
        
        return customer, "Cliente criado com sucesso"
        
    except IntegrityError as e:
        db.session.rollback()
        if 'ds_customer_email' in str(e):
            return None, "Email já está em uso"
        elif 'ds_customer_cpf_cnpj' in str(e):
            return None, "CPF/CNPJ já está em uso"
        else:
            return None, "Erro de integridade no banco de dados"
    except Exception as e:
        db.session.rollback()
        return None, f"Erro ao criar cliente: {str(e)}"

def get_all_customers(active_only=True, page=1, per_page=20):
    """
    Retorna lista paginada de clientes.
    
    Args:
        active_only (bool): Se True, retorna apenas clientes ativos
        page (int): Número da página
        per_page (int): Itens por página
        
    Returns:
        dict: Contém customers, total, pages, current_page
    """
    try:
        query = Customer.query
        
        if active_only:
            query = query.filter(Customer.is_customer_active == True)
        
        query = query.order_by(Customer.ds_customer_name)
        
        paginated = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        return {
            'customers': [customer.to_dict() for customer in paginated.items],
            'total': paginated.total,
            'pages': paginated.pages,
            'current_page': page,
            'per_page': per_page
        }
        
    except Exception as e:
        return {
            'customers': [],
            'total': 0,
            'pages': 0,
            'current_page': page,
            'per_page': per_page,
            'error': f"Erro ao buscar clientes: {str(e)}"
        }

def get_customer_by_id(customer_id):
    """
    Busca um cliente pelo ID.
    
    Args:
        customer_id (str): UUID do cliente
        
    Returns:
        tuple: (Customer object or None, message)
    """
    try:
        customer = Customer.query.filter_by(cd_customer=customer_id).first()
        
        if not customer:
            return None, "Cliente não encontrado"
        
        return customer, "Cliente encontrado"
        
    except Exception as e:
        return None, f"Erro ao buscar cliente: {str(e)}"

def update_customer(customer_id, customer_data):
    """
    Atualiza os dados de um cliente.
    
    Args:
        customer_id (str): UUID do cliente
        customer_data (dict): Novos dados do cliente
        
    Returns:
        tuple: (Customer object or None, message)
    """
    try:
        customer = Customer.query.filter_by(cd_customer=customer_id).first()
        
        if not customer:
            return None, "Cliente não encontrado"
        
        # Atualizar campos permitidos
        updatable_fields = [
            'ds_customer_name', 'ds_customer_email', 'ds_customer_phone',
            'ds_customer_cpf_cnpj', 'ds_customer_address', 'ds_customer_city',
            'ds_customer_state', 'ds_customer_zip_code', 'ds_customer_country'
        ]
        
        for field in updatable_fields:
            if field in customer_data:
                setattr(customer, field, customer_data[field])
        
        # Atualizar timestamp
        customer.dt_customer_updated_at = datetime.utcnow()
        
        # Validar CPF/CNPJ se foi alterado
        if not customer.validate_cpf_cnpj():
            return None, "CPF/CNPJ em formato inválido"
        
        db.session.commit()
        
        return customer, "Cliente atualizado com sucesso"
        
    except IntegrityError as e:
        db.session.rollback()
        if 'ds_customer_email' in str(e):
            return None, "Email já está em uso por outro cliente"
        elif 'ds_customer_cpf_cnpj' in str(e):
            return None, "CPF/CNPJ já está em uso por outro cliente"
        else:
            return None, "Erro de integridade no banco de dados"
    except Exception as e:
        db.session.rollback()
        return None, f"Erro ao atualizar cliente: {str(e)}"

def delete_customer(customer_id, soft_delete=True):
    """
    Remove um cliente (soft delete por padrão).
    
    Args:
        customer_id (str): UUID do cliente
        soft_delete (bool): Se True, apenas marca como inativo
        
    Returns:
        tuple: (bool, message)
    """
    try:
        customer = Customer.query.filter_by(cd_customer=customer_id).first()
        
        if not customer:
            return False, "Cliente não encontrado"
        
        if soft_delete:
            # Soft delete - apenas marca como inativo
            customer.is_customer_active = False
            customer.dt_customer_updated_at = datetime.utcnow()
            db.session.commit()
            return True, "Cliente desativado com sucesso"
        else:
            # Hard delete - remove completamente
            db.session.delete(customer)
            db.session.commit()
            return True, "Cliente removido com sucesso"
        
    except Exception as e:
        db.session.rollback()
        return False, f"Erro ao remover cliente: {str(e)}"

def search_customers(search_term, search_fields=None, active_only=True):
    """
    Busca clientes por termo de pesquisa.
    
    Args:
        search_term (str): Termo de pesquisa
        search_fields (list): Campos para buscar ['name', 'email', 'cpf_cnpj']
        active_only (bool): Se True, busca apenas clientes ativos
        
    Returns:
        list: Lista de clientes encontrados
    """
    try:
        if not search_term:
            return []
        
        if search_fields is None:
            search_fields = ['name', 'email', 'cpf_cnpj']
        
        query = Customer.query
        
        if active_only:
            query = query.filter(Customer.is_customer_active == True)
        
        conditions = []
        search_term = f"%{search_term}%"
        
        if 'name' in search_fields:
            conditions.append(Customer.ds_customer_name.ilike(search_term))
        if 'email' in search_fields:
            conditions.append(Customer.ds_customer_email.ilike(search_term))
        if 'cpf_cnpj' in search_fields:
            conditions.append(Customer.ds_customer_cpf_cnpj.ilike(search_term))
        
        if conditions:
            query = query.filter(db.or_(*conditions))
        
        customers = query.order_by(Customer.ds_customer_name).all()
        
        return [customer.to_dict() for customer in customers]
        
    except Exception as e:
        return []

def activate_customer(customer_id):
    """
    Reativa um cliente desativado.
    
    Args:
        customer_id (str): UUID do cliente
        
    Returns:
        tuple: (bool, message)
    """
    try:
        customer = Customer.query.filter_by(cd_customer=customer_id).first()
        
        if not customer:
            return False, "Cliente não encontrado"
        
        customer.is_customer_active = True
        customer.dt_customer_updated_at = datetime.utcnow()
        db.session.commit()
        
        return True, "Cliente reativado com sucesso"
        
    except Exception as e:
        db.session.rollback()
        return False, f"Erro ao reativar cliente: {str(e)}"