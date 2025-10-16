# app/models/interaction_model.py

import enum
from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class InteractionType(enum.Enum):
    VENDA = 'venda'
    LIGACAO = 'ligacao'
    EMAIL = 'email'
    REUNIAO = 'reuniao'
    CONTATO = 'contato' # Genérico

class Interaction(db.Model):
    __tablename__ = 'interaction'
    
    cd_interaction = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Chaves estrangeiras para ligar a interação ao cliente e ao usuário
    cd_customer = db.Column(UUID(as_uuid=True), db.ForeignKey('customer.cd_customer'), nullable=False, index=True)
    cd_user = db.Column(UUID(as_uuid=True), db.ForeignKey('user.cd_user'), nullable=False)

    # O que aconteceu na interação
    ds_notes = db.Column(db.Text, nullable=False)
    id_interaction_type = db.Column(db.Enum(InteractionType), nullable=False, default=InteractionType.CONTATO)
    
    # Quando a interação aconteceu
    dt_interaction = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Campos de controle
    dt_created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dt_updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Interaction {self.cd_interaction}>'