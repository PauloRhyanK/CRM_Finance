from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class TransactionType(enum.Enum):
    ENTRADA = 1
    SAIDA = 2

class Transaction(db.Model):
    __tablename__ = 'transaction'

    cd_transaction = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vr_transaction = db.Column(db.Numeric(10, 2), nullable=False)    
       
    # Ex: 1 = Entrada, 2 = Saída
    id_transaction_type = db.Column(db.Enum(TransactionType), nullable=False)
    
    dt_transaction = db.Column(db.Date, nullable=False)
    dt_transaction_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    cd_user = db.Column(UUID(as_uuid=True), db.ForeignKey('user.cd_user'), nullable=False)
    cd_customer = db.Column(UUID(as_uuid=True), db.ForeignKey('customer.cd_customer'), nullable=False)