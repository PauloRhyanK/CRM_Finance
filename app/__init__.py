from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

# Cria instâncias das extensões
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='development'):
    """
    Função Application Factory.
    """
    # Cria e configura a aplicação Flask
    app = Flask(__name__)

    if config_name == "development":
        app.config.from_object('config.DevelopmentConfig')
    elif config_name == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DefaultConfig')

    app.debug = app.config.get('DEBUG', False)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app