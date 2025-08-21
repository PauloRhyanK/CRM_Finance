# Arquivo: app/models/user_model.py

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    # --- Colunas da Tabela ---
    cd_user = db.Column(db.Integer, primary_key=True)
    ds_user = db.Column(db.String(100), nullable=False)
    ds_user_email = db.Column(db.String(100), unique=True, nullable=False) # ADICIONADO: unique=True, nullable=False
    
    # MUDANÇA: Renomeado para password_hash para deixar claro o que guardamos
    password_hash = db.Column(db.String(128), nullable=False)
    
    # MUDANÇA: Usando db.Date e removendo onupdate
    dt_user_nasc = db.Column(db.Date, nullable=False) 
    
    dt_user_create = db.Column(db.DateTime, default=datetime.utcnow)
    
    cd_role = db.Column(db.Integer, db.ForeignKey('roles.cd_role'), nullable=False)

    # --- Métodos de Instância ---
    
    def set_password(self, password):
        """Cria um hash da senha e o armazena."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica se a senha fornecida corresponde ao hash armazenado."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Representação em string do objeto, útil para depuração."""
        return f'<User {self.ds_user}>'