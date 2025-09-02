# Arquivo: config.py

import os
from dotenv import load_dotenv

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
    

    SQLALCHEMY_DATABASE_URI = 'sqlite:///crm_finance.db'
    
    # Configuração PostgreSQL (comentada para desenvolvimento local)
    # DB_USER = os.getenv('POSTGRES_USER', 'default_user')
    # DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'default_password') 
    # DB_NAME = os.getenv('POSTGRES_DB', 'default_db') 
    # DB_HOST = 'db' 
    # SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'

class ProductionConfig(DefaultConfig):
    DEBUG = False
    ENV = 'production'
