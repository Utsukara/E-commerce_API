from models.customer import Customer
from models.order import Order
from models.product import Product
from database import db
from sqlalchemy.orm import Session
from sqlalchemy import select

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            
            product_ids = [product['id'] for product in order_data['products']]
            products = session.execute(select(Product).filter(Product.id.in_(product_ids))).scalars().all()

            customer_id = order_data['customer_id']
            customer = session.execute(select(Customer).filter(Customer.id == customer_id)).scalar_one()

            if len(products) != len(product_ids):
                raise ValueError('Product not found')
            
            if not customer:
                raise ValueError('Customer not found')
            
            print('Products:', products[0].name)
            new_order = Order(date=order_data['date'], customer_id=order_data['customer_id'], products=products)
            session.add(new_order)
            print('New order ID(before commit):', new_order.id)
            session.flush()
            print('New order ID(after commit):', new_order.id)
            session.commit()

        session.refresh(new_order)

        for product in new_order.products:
            session.refresh(product)

        return new_order
    
def find_by_id(id):
    query = select(Order).join(Customer).where(Customer.id == Order.customer_id).filter_by(id=id)
    order = db.session.execute(query).scalar_one_or_none()
    return order