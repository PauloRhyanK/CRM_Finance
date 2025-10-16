from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_object):  # <- MUDANÇA 1: Recebe o objeto de config
    """
    Função Application Factory.
    """
    app = Flask(__name__)

    # Carrega a configuração diretamente do objeto recebido
    app.config.from_object(config_object) # <- MUDANÇA 2

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import User, Transaction, Customer  

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .main.routes.route_manager import register_all_routes
    register_all_routes(app)

    return app