from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String
from database import Base

class Customer(Base):
    __tablename__ = 'customers'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(329))
    phone: Mapped[str] = mapped_column(String(15))
    
    # One-to-one relationship with CustomerAccount
    customer_account: Mapped['CustomerAccount'] = relationship('CustomerAccount', back_populates='customer', uselist=False)
    
    # One-to-many relationship with Order
    orders: Mapped[List['Order']] = relationship('Order', back_populates='customer')

