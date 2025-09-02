# Arquivo: app/main/routes/route_manager.py

import os
import importlib
from flask import Blueprint

def register_all_routes(app):
    """
    Função que automaticamente descobre e registra todas as rotas
    definidas como Blueprints no diretório routes.
    """
    routes_dir = os.path.dirname(__file__)
    
    for filename in os.listdir(routes_dir):
        if filename.endswith('.py') and not filename.startswith('__') and filename != 'route_manager.py':
    
            module_name = filename[:-3]
            
            try:
        
                module = importlib.import_module(f'app.main.routes.{module_name}')
                
        
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
            
                    if isinstance(attr, Blueprint):
                        app.register_blueprint(attr)
                        print(f"[DEBUG] Blueprint '{attr.name}' registrado de {module_name}.py")
                        
            except ImportError as e:
                print(f"[WARNING] Erro ao importar {module_name}.py: {e}")
                continue

def get_all_blueprints():
    """
    Função alternativa que retorna uma lista de todos os blueprints
    para uso manual se necessário.
    """
    blueprints = []
    
    try:
        from .auth_routes import auth_bp
        blueprints.append(auth_bp)
    except ImportError:
        pass
        
    
    return blueprints
