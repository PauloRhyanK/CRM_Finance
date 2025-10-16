from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class Customer(db.Model):
    __tablename__ = 'customer'
    
    cd_customer = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ds_customer_name = db.Column(db.String(255), nullable=False)
    ds_customer_email = db.Column(db.String(255), unique=True, nullable=False)
    ds_customer_phone = db.Column(db.String(20), nullable=True)
    ds_customer_cpf_cnpj = db.Column(db.String(18), unique=True, nullable=True)  # Pode ser CPF ou CNPJ
    
    # Campos de endereço
    ds_customer_address = db.Column(db.String(500), nullable=True)
    ds_customer_city = db.Column(db.String(100), nullable=True)
    ds_customer_state = db.Column(db.String(2), nullable=True)  # UF
    ds_customer_zip_code = db.Column(db.String(10), nullable=True)
    ds_customer_country = db.Column(db.String(100), nullable=True, default='Brasil')
    
    # Campos de controle
    dt_customer_created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dt_customer_updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.utcnow)
    is_customer_active = db.Column(db.Boolean, nullable=False, default=True)
    
    transactions = db.relationship('Transaction', backref='customer', lazy=True)    
    
    def to_dict(self):
        """Converte o objeto Customer para dicionário"""
        return {
            'cd_customer': str(self.cd_customer),
            'ds_customer_name': self.ds_customer_name,
            'ds_customer_email': self.ds_customer_email,
            'ds_customer_phone': self.ds_customer_phone,
            'ds_customer_cpf_cnpj': self.ds_customer_cpf_cnpj,
            'ds_customer_address': self.ds_customer_address,
            'ds_customer_city': self.ds_customer_city,
            'ds_customer_state': self.ds_customer_state,
            'ds_customer_zip_code': self.ds_customer_zip_code,
            'ds_customer_country': self.ds_customer_country,
            'dt_customer_created_at': self.dt_customer_created_at.isoformat() if self.dt_customer_created_at else None,
            'dt_customer_updated_at': self.dt_customer_updated_at.isoformat() if self.dt_customer_updated_at else None,
            'is_customer_active': self.is_customer_active
        }
    
    def validate_cpf_cnpj(self):
        """Valida se o CPF/CNPJ está em formato válido"""
        if not self.ds_customer_cpf_cnpj:
            return True  # Campo opcional
        
        # Remove caracteres especiais
        cpf_cnpj = ''.join(filter(str.isdigit, self.ds_customer_cpf_cnpj))
        
        # Verifica se é CPF (11 dígitos) ou CNPJ (14 dígitos)
        return len(cpf_cnpj) in [11, 14]
    
    def __repr__(self):
        return f'<Customer {self.ds_customer_name} - {self.ds_customer_email}>'