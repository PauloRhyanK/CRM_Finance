from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

# Cria instâncias das extensões
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=DevelopmentConfig):
    """
    Função Application Factory.
    """
    # Cria e configura a aplicação Flask
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializa as extensões com a aplicação
    db.init_app(app)
    migrate.init_app(app, db)
    
    # --- Registro dos Blueprints (Rotas) ---
    # (Adicionaremos nossas rotas aqui no futuro)
    # Ex: from app.routes.auth_routes import auth_bp
    #     app.register_blueprint(auth_bp)

    @app.route('/health')
    def health_check():
        return "<h1>A aplicação está no ar e funcionando!</h1>", 200

    return app