from typing import List
import datetime
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Column, Integer, Date, ForeignKey
from database import Base
from models.orderProduct import order_product

class Order(Base):
    __tablename__ = 'orders'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.id'))
    
    customer: Mapped['Customer'] = relationship('Customer', back_populates='orders')
    products: Mapped[List['Product']] = relationship('Product', secondary=order_product)

