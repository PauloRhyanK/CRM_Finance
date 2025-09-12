from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='development'):
    """
    Função Application Factory.
    """
    app = Flask(__name__)

    if config_name == "development":
        app.config.from_object('config.DevelopmentConfig')
    elif config_name == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DefaultConfig')

    print(app.config)
    
    app.debug = app.config.get('DEBUG', False)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import User, Transaction  

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .main.routes.route_manager import register_all_routes
    register_all_routes(app)

    return app