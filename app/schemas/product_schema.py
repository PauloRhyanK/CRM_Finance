# app/schemas/product_schema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
from app.models.product_model import Product

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_fk = True

    ds_product_name = fields.Str(required=True, validate=validate.Length(min=3, max=255))
    vr_price = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    id_product_type = fields.Str(required=True, validate=validate.OneOf(['produto', 'servico']))