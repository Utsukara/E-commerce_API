from marshmallow import validate, fields
from schema import ma

class ProductSchema(ma.Schema):
    id = ma.Integer(required=False)
    name = ma.String(required=True, validate=validate.Length(min=1))
    price = ma.Float(required=True, validate=validate.Range(min=0))
    #stock = ma.Integer(required=True, validate=validate.Range(min=0))

class ProductSchemaID(ma.Schema):
    id = fields.Integer(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)