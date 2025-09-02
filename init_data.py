# Arquivo: init_data.py

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import User, Role

def init_roles():
    """Cria roles padrão no sistema"""
    
    if Role.query.first():
        print("Roles já existem no banco de dados.")
        return
    
    roles = [
        {'cd_role': 1, 'ds_role': 'admin', 'ds_description': 'Administrador do sistema'},
        {'cd_role': 2, 'ds_role': 'user', 'ds_description': 'Usuário comum'},
        {'cd_role': 3, 'ds_role': 'manager', 'ds_description': 'Gerente'}
    ]
    
    for role_data in roles:
        role = Role(
            cd_role=role_data['cd_role'],
            ds_role=role_data['ds_role'],
            ds_description=role_data['ds_description']
        )
        db.session.add(role)
    
    db.session.commit()
    print("Roles criados com sucesso!")

def create_admin_user():
    """Cria um usuário administrador padrão"""
    
    admin = User.query.filter_by(ds_user_email='admin@admin.com').first()
    if admin:
        print("Usuário admin já existe.")
        return
    
    from datetime import date
    
    admin_user = User(
        ds_user='admin',
        ds_user_email='admin@admin.com',
        dt_user_nasc=date(1990, 1, 1),
        cd_role=1 
        )
    admin_user.set_password('admin123')
    
    db.session.add(admin_user)
    db.session.commit()
    print("Usuário admin criado: admin@admin.com / admin123")

if __name__ == '__main__':
    app = create_app('development')
    
    with app.app_context():
        print("Inicializando dados...")
        init_roles()
        create_admin_user()
        print("Dados iniciais criados com sucesso!")
