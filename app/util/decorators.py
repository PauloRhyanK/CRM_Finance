# app/util/decorators.py

from functools import wraps
from flask import jsonify
import uuid

def validate_uuid(param_name):
    """
    Decorador para validar se um parâmetro da rota é um UUID válido.
    Retorna um erro 400 (Bad Request) se a validação falhar.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # kwargs contém os parâmetros da URL, como 'customer_id'
            if param_name not in kwargs:
                # Este erro é para o desenvolvedor, não deveria acontecer em produção
                return jsonify({'error': f'Parâmetro de rota {param_name} ausente'}), 500
            
            try:
                # Tenta converter o parâmetro para um objeto UUID
                uuid.UUID(kwargs[param_name])
            except ValueError:
                # Se falhar, retorna um erro claro para o cliente da API
                return jsonify({'error': f'O ID fornecido para {param_name} não é um UUID válido'}), 400
            
            # Se a validação passar, executa a função da rota original
            return f(*args, **kwargs)
        return decorated_function
    return decorator