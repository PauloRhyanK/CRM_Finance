# config.py
import os

# A pasta base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

# Não precisamos mais do load_dotenv aqui, o Docker Compose já injeta as variáveis.

class Config:
    """Configurações base que servem para todos os ambientes."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False # Garante que a API responda em UTF-8

    # A string de conexão é montada uma única vez, usando as variáveis de ambiente
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    DB_NAME = os.environ.get('POSTGRES_DB')
    DB_HOST = os.environ.get('DB_HOST') # Virá do .env ('db')

    # A STRING DE CONEXÃO CORRETA E ÚNICA!
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
        '?client_encoding=utf8'
    )

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurações para produção."""
    DEBUG = False

# Mapeamento para facilitar a seleção no create_app
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}