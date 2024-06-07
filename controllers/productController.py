from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError

def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    try:
        product_save = productService.save(product_data)
        return product_schema.jsonify(product_save), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400