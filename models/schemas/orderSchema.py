from marshmallow import fields
from schema import ma

class OrderSchema(ma.Schema):
    id = ma.Integer(required=False)
    date = ma.Date(required=True)
    customer_id = ma.Integer(required=True)
    products = fields.Nested('ProductSchemaID', many=True)

class OrderSchemaCustomer(ma.Schema):
    id = ma.Integer(required=False)
    date = ma.Date(required=True)
    customer = ma.Nested('CustomerSchema')
    products = fields.Nested('ProductSchema', many=True)

order_schema_customer = OrderSchemaCustomer()

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)