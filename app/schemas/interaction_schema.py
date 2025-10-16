# app/schemas/interaction_schema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
from app.models.interaction_model import Interaction

class InteractionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Interaction
        load_instance = True
        include_fk = True

    # Validação explícita para os campos mais importantes
    ds_notes = fields.Str(required=True, validate=validate.Length(min=5))
    cd_customer = fields.UUID(required=True)
    cd_user = fields.UUID(required=True)
    id_interaction_type = fields.Str(
        required=True, 
        validate=validate.OneOf(['venda', 'ligacao', 'email', 'reuniao', 'contato'])
    )