# Arquivo: config.py

import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
# Isso garante que os.getenv() encontre nossas variáveis
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Configurações base que servem para qualquer ambiente."""
    # Desativa um recurso do SQLAlchemy que não usaremos e que emite avisos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config): # Adicionamos a herança de Config
    """Configurações específicas para o ambiente de desenvolvimento."""
    DEBUG = True # Ativa o modo de depuração do Flask
    
    # Busca cada variável de ambiente com seu nome correto
    DB_USER = os.getenv('POSTGRES_USER', 'default_user')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'default_password') # CORRIGIDO
    DB_NAME = os.getenv('POSTGRES_DB', 'default_db') # CORRIGIDO
    DB_HOST = 'db' # Nome do serviço do postgres no seu docker-compose.yml
    
    # Monta a string de conexão do banco de dados
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'