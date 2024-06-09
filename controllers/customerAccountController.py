from models.schemas.customerAccountSchema import customer_account_schema, customer_accounts_schema
from services import customerAccountService
from flask import request, jsonify

def find_all():
    customer_accounts = customerAccountService.find_all()
    return customer_accounts_schema.jsonify(customer_accounts), 200

def login():
    customer = request.json
    user = customerAccountService.login_customer(customer['username'], customer['password'])
    if user:
        return jsonify(user), 200
    else:
        resp = {
            'status': 'Error',
            'message': 'Invalid username or password'
        }
        return jsonify(resp), 404