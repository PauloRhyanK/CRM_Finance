# app/services/product_service.py

from app import db
from app.models.product_model import Product
from app.schemas.product_schema import ProductSchema
from app.util.exceptions import ProductNotFoundError, InvalidDataError
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

def create_product(product_data):
    """Cria um novo produto. Levanta exceções em caso de erro."""
    try:
        product = product_schema.load(product_data)
        db.session.add(product)
        db.session.commit()
        return product
    except ValidationError as err:
        raise InvalidDataError(err.messages)
    except IntegrityError:
        db.session.rollback()
        raise InvalidDataError("Um produto com este nome já existe.")

def get_product_by_id(product_id):
    """Busca um produto pelo ID. Levanta ProductNotFoundError se não encontrar."""
    product = Product.query.filter_by(cd_product=product_id).first()
    if not product:
        raise ProductNotFoundError()
    return product

def update_product(product_id, product_data):
    """Atualiza um produto. Levanta ProductNotFoundError ou InvalidDataError."""
    product = get_product_by_id(product_id)  

    try:
        updated_product = product_schema.load(
            product_data, instance=product, partial=True, session=db.session
        )
        
        db.session.commit()
        return updated_product
    except ValidationError as err:
        raise InvalidDataError(err.messages)
    except IntegrityError:
        db.session.rollback()
        raise InvalidDataError("Um produto com este nome já existe.")

def delete_product(product_id, soft_delete=True):
    """Remove um produto (soft ou hard delete)."""
    product = get_product_by_id(product_id)
    
    if soft_delete:
        product.is_active = False
    else:
        db.session.delete(product)
    
    db.session.commit()
    
    return True

def get_all_products(page=1, per_page=20, active_only=True):
    """Retorna uma lista paginada de produtos."""
    query = Product.query
    if active_only:
        query = query.filter(Product.is_active == True)
    
    paginated = query.order_by(Product.ds_product_name).paginate(
        page=page, per_page=per_page, error_out=False
    )
    return paginated
