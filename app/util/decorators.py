# app/util/decorators.py
from functools import wraps
from flask import jsonify
import uuid

def validate_uuid(param_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if param_name not in kwargs:
                return jsonify({'error': f'Parâmetro {param_name} ausente'}), 500
            
            try:
                uuid.UUID(kwargs[param_name])
            except ValueError:
                return jsonify({'error': f'ID inválido para {param_name}'}), 400
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator