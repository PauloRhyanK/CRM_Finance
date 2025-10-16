# app/schemas/customer_schema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.customer_model import Customer

class CustomerSchema(SQLAlchemyAutoSchema):
    """
    Esquema de serialização e validação para o modelo Customer.
    
    `SQLAlchemyAutoSchema` gera automaticamente os campos do esquema
    a partir do modelo SQLAlchemy.
    """
    class Meta:
        model = Customer
        load_instance = True  # Deserializa para um objeto Customer
        include_fk = True     # Inclui chaves estrangeiras na serialização

    ds_customer_email = fields.Email(required=True)