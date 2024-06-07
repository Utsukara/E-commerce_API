from flask import Blueprint
from controllers.customerController import save, find_all, find_customer_by_gmail, find_all_pagination

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/gmail', methods=['GET'])(find_customer_by_gmail)
customer_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)