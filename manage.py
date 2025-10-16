# manage.py (CORRIGIDO E SIMPLIFICADO)

import os
from app import create_app, db
from config import config_by_name
from flask_migrate import Migrate

# Carrega a configuração do ambiente
config_name = os.getenv('FLASK_ENV', 'default')
config_object = config_by_name[config_name]

# Cria a instância da aplicação
app = create_app(config_object)

# Associa a instância da aplicação com o Migrate
migrate = Migrate(app, db)

# O CLI do Flask/Flask-Migrate automaticamente encontra a variável 'app'
# e a instância 'migrate' neste ficheiro. Não precisamos de mais nada.