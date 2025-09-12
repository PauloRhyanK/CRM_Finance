from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user' # Define o nome da tabela

    cd_user = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ds_user = db.Column(db.String(255), nullable=False)
    ds_user_email = db.Column(db.String(255), unique=True, nullable=False)
    
    # Esta coluna guardará o "hash" da senha.
    password_hash = db.Column(db.String(255), nullable=False)
    
    dt_user_createdat = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dt_user_last_login = db.Column(db.DateTime, nullable=True) # Nullable, pois o user ainda não logou ao ser criado

    transactions = db.relationship('Transaction', backref='user', lazy=True)
    
    def set_password(self, password):
        """Cria o hash da senha e armazena no campo password_hash"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica se a senha fornecida corresponde ao hash armazenado"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.ds_user_email}>'