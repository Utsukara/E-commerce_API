from sqlalchemy import select
from models.customer import Customer
from models.customer_account import CustomerAccount
from database import db

def find_all():
    query = select(CustomerAccount).join(Customer).where(Customer.id == CustomerAccount.customer_id)
    customer_accounts = db.session.execute(query).scalars().all()
    return customer_accounts