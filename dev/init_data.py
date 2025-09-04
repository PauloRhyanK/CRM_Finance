# Arquivo: init_data.py

import os
import sys

# Adiciona o diretório pai ao path para importar os módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from app import create_app, db
from app.models.user_model import User
from app.models.transaction_model import Transaction
from datetime import datetime, date
from werkzeug.security import generate_password_hash

def create_admin_user():
    """Cria um usuário administrador padrão"""
    
    admin = User.query.filter_by(ds_user_email='admin@admin.com').first()
    if admin:
        print("Usuário admin já existe.")
        return
    
    admin_user = User(
        ds_user='admin',
        ds_user_email='admin@admin.com',
        password_hash=generate_password_hash('admin123')
    )
    
    db.session.add(admin_user)
    db.session.commit()
    print("Usuário admin criado: admin@admin.com / admin123")

def create_sample_user():
    """Cria um usuário de exemplo"""
    
    user = User.query.filter_by(ds_user_email='user@example.com').first()
    if user:
        print("Usuário de exemplo já existe.")
        return
    
    sample_user = User(
        ds_user='João Silva',
        ds_user_email='user@example.com',
        password_hash=generate_password_hash('123456')
    )
    
    db.session.add(sample_user)
    db.session.commit()
    print("Usuário de exemplo criado: user@example.com / 123456")
    return sample_user

def create_sample_transactions():
    """Cria transações de exemplo"""
    
    # Verifica se já existem transações
    if Transaction.query.first():
        print("Transações de exemplo já existem.")
        return
    
    # Busca um usuário para associar as transações
    user = User.query.filter_by(ds_user_email='user@example.com').first()
    if not user:
        print("Criando usuário de exemplo primeiro...")
        user = create_sample_user()
    
    # Transações de exemplo
    transactions = [
        {
            'vr_transaction': 1500.00,
            'id_transaction_type': 1,  # Entrada
            'dt_transaction': date(2024, 9, 1),
            'cd_user': user.cd_user
        },
        {
            'vr_transaction': -350.00,
            'id_transaction_type': 2,  # Saída
            'dt_transaction': date(2024, 9, 2),
            'cd_user': user.cd_user
        },
        {
            'vr_transaction': 2000.00,
            'id_transaction_type': 1,  # Entrada
            'dt_transaction': date(2024, 9, 3),
            'cd_user': user.cd_user
        },
        {
            'vr_transaction': -120.50,
            'id_transaction_type': 2,  # Saída
            'dt_transaction': date(2024, 9, 4),
            'cd_user': user.cd_user
        }
    ]
    
    for trans_data in transactions:
        transaction = Transaction(
            vr_transaction=trans_data['vr_transaction'],
            id_transaction_type=trans_data['id_transaction_type'],
            dt_transaction=trans_data['dt_transaction'],
            cd_user=trans_data['cd_user']
        )
        db.session.add(transaction)
    
    db.session.commit()
    print(f"Criadas {len(transactions)} transações de exemplo.")
if __name__ == '__main__':
    app = create_app('development')
    
    with app.app_context():
        print("=" * 50)
        print("🚀 Inicializando dados de exemplo...")
        print("=" * 50)
        
        try:
            create_admin_user()
            create_sample_user()
            create_sample_transactions()
            
            print("=" * 50)
            print("✅ Dados iniciais criados com sucesso!")
            print("=" * 50)
            print("👤 Usuários criados:")
            print("   Admin: admin@admin.com / admin123")
            print("   User:  user@example.com / 123456")
            print("")
            print("💰 Transações de exemplo criadas")
            print("=" * 50)
            
        except Exception as e:
            print(f"❌ Erro ao criar dados: {e}")
            db.session.rollback()
