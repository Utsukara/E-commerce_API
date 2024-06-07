from flask import Blueprint
from controllers.productController import save

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/s', methods=['POST'])(save)