from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from circuitbreaker import circuit
from sqlalchemy import select

def fallback_function(customer):
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_function)
def save(customer_data):
    try:
        if customer_data['name'] == 'Failure':
            raise Exception('Failure condition triggered')
        
        with Session(db.engine) as session:
            with session.begin():
                new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
                session.add(new_customer)
                session.commit()
                session.refresh(new_customer)
            return new_customer
    except Exception as e:
        raise e

def find_all():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers

def find_customer_by_gmail():
    query = select(Customer).where(Customer.email.like('%gmail%'))
    customers = db.session.execute(query).scalars().all()
    return customers

def find_all_pagination(page = 1, per_page = 10):
    customers = db.paginate(select(Customer), page=page, per_page=per_page)
    return customers