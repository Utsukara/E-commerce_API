from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_save = customerService.save(customer_data)
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else:
        return jsonify({'message': 'Fallback method error activated', 'body': customer_data}), 400

@cache.cached(timeout=60)
def find_all():
    customers = customerService.find_all()
    return customers_schema.jsonify(customers), 200

def find_customer_by_gmail():
    customers = customerService.find_customer_by_gmail()
    return customers_schema.jsonify(customers), 200

def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return customers_schema.jsonify(customerService.find_all_pagination(page=page, per_page=per_page)), 200