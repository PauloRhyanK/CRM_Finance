from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

# Esta instância 'db' normalmente é criada no seu arquivo app/__init__.py
db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__ = 'transaction'

    cd_transaction = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vr_transaction = db.Column(db.Float, nullable=False)
    
    # Ex: 1 = Entrada, 2 = Saída
    id_transaction_type = db.Column(db.Integer, nullable=False)
    
    dt_transaction = db.Column(db.Date, nullable=False)
    dt_transaction_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    cd_user = db.Column(UUID(as_uuid=True), db.ForeignKey('user.cd_user'), nullable=False)