# Arquivo: config.py

import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class DefaultConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave-padrao-insegura')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    TESTING = True
    ENV = 'development'
    FLASK_DEBUG = 1
    """Configurações específicas para o ambiente de desenvolvimento."""
    
    # PostgreSQL para desenvolvimento (mantém paridade com produção)
    DB_USER = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', '1234') 
    DB_NAME = os.getenv('POSTGRES_DB', 'crm_db') 
    DB_HOST = os.getenv('DB_HOST', 'localhost')  # localhost para dev local, 'db' para Docker
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
    
    # SQLite como fallback (descomente se não tiver PostgreSQL instalado)
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///crm_finance.db'

class ProductionConfig(DefaultConfig):
    DEBUG = False
    ENV = 'production'
    
    # Em produção, sempre use PostgreSQL
    DB_USER = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', '1234') 
    DB_NAME = os.getenv('POSTGRES_DB', 'crm_db') 
    DB_HOST = os.getenv('DB_HOST', 'db')  # Container name no Docker
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
