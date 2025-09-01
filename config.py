# Arquivo: config.py

import os
from dotenv import load_dotenv

class DefaultConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave-padrao-insegura')

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    TESTING = True
    ENV = 'development'
    FLASK_DEBUG = 1
     """Configurações específicas para o ambiente de desenvolvimento."""
    
    # Busca cada variável de ambiente com seu nome correto
    DB_USER = os.getenv('POSTGRES_USER', 'default_user')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'default_password') # CORRIGIDO
    DB_NAME = os.getenv('POSTGRES_DB', 'default_db') # CORRIGIDO
    DB_HOST = 'db' # Nome do serviço do postgres no seu docker-compose.yml
    
    # Monta a string de conexão do banco de dados
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'

class ProductionConfig(DefaultConfig):
    DEBUG = False
    ENV = 'production'
