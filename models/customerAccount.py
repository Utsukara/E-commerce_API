from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class CustomerAccount(Base):
    __tablename__ = 'customer_accounts'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.id'))
    
    # One-to-one relationship with Customer
    customer: Mapped['Customer'] = relationship('Customer', back_populates='customer_account', lazy='select')
    
    # Many-to-many relationship with Role
    roles: Mapped[list['Role']] = relationship('Role', secondary='customer_management_roles')