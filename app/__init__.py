from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .util.exceptions import ServiceError

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_object):  # <- MUDANÇA 1: Recebe o objeto de config
    """
    Função Application Factory.
    """
    app = Flask(__name__)

    app.config.from_object(config_object) 
    db.init_app(app)
    migrate.init_app(app, db)

    @app.errorhandler(ServiceError)
    def handle_service_error(error):
        """Captura todas as exceções do tipo ServiceError e formata a resposta JSON."""
        response = jsonify({'error': str(error)})
        response.status_code = error.status_code
        return response

    from . import models
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .main.routes.route_manager import register_all_routes
    register_all_routes(app)

    return app