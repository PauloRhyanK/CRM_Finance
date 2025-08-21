"""
Database Manager Simples - Para aprendizado
"""
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

class DatabaseManager:
    """
    Classe simples para gerenciar banco de dados
    """
    
    def __init__(self):
        self.db = SQLAlchemy()
    
    def init_app(self, app):
        """Inicializa o banco com a aplicação Flask"""
        # Configurações básicas
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///crm.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        # Inicializa SQLAlchemy
        self.db.init_app(app)
        print(f"✅ Banco configurado: {self._get_db_type()}")
    
    def _get_db_type(self):
        """Identifica o tipo de banco"""
        url = os.environ.get('DATABASE_URL', 'sqlite:///crm.db')
        if 'postgresql' in url:
            return 'PostgreSQL'
        elif 'mysql' in url:
            return 'MySQL'
        else:
            return 'SQLite'
    
    def create_tables(self):
        """Cria todas as tabelas"""
        try:
            self.db.create_all()
            print("✅ Tabelas criadas com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar tabelas: {e}")
            return False
    
    def reset_tables(self):
        """Remove e recria todas as tabelas"""
        try:
            self.db.drop_all()
            self.db.create_all()
            print("✅ Banco resetado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao resetar banco: {e}")
            return False
    
    def test_connection(self):
        """Testa se a conexão está funcionando"""
        try:
            # Testa uma query simples
            result = self.db.session.execute('SELECT 1')
            return {"status": "ok", "database": self._get_db_type()}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    
# Instância global
db_manager = DatabaseManager()
        