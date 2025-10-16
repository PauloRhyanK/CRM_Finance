# app/services/interaction_service.py

from app import db
from app.models.interaction_model import Interaction
from app.models.customer_model import Customer # Para verificar se o cliente existe
from app.schemas.interaction_schema import InteractionSchema
from app.util.exceptions import InvalidDataError, CustomerNotFoundError
from marshmallow import ValidationError

interaction_schema = InteractionSchema()
interactions_schema = InteractionSchema(many=True)

def create_interaction(interaction_data):
    """Cria um novo registro de interação."""
    try:
        # Primeiro, verifica se o cliente associado existe
        customer_id = interaction_data.get('cd_customer')
        if not Customer.query.filter_by(cd_customer=customer_id).first():
            raise CustomerNotFoundError()

        interaction = interaction_schema.load(interaction_data)
        
        db.session.add(interaction)
        db.session.commit()
        return interaction
    except ValidationError as err:
        raise InvalidDataError(err.messages)

def get_interactions_for_customer(customer_id, page=1, per_page=15):
    """Retorna uma lista paginada de interações para um cliente específico."""
    # Verifica se o cliente existe primeiro
    if not Customer.query.filter_by(cd_customer=customer_id).first():
        raise CustomerNotFoundError()
        
    paginated = Interaction.query.filter_by(cd_customer=customer_id)\
        .order_by(Interaction.dt_interaction.desc())\
        .paginate(page=page, per_page=per_page, error_out=False)
        
    return paginated