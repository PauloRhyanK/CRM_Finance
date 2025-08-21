from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_migrate import Migrate
from database.config import DevelopmentConfig 
from util.database import db_manager

load_dotenv()
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

# Inicializa o DatabaseManager (simples!)
db_manager.init_app(app)
db = db_manager.db
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/db/status")
def database_status():
    """Verifica se banco está funcionando"""
    status = db_manager.test_connection()
    return jsonify(status)

if __name__ == '__main__':
    # Criar tabelas ao iniciar
    with app.app_context():
        db_manager.create_tables()
    
    app.run(debug=True)