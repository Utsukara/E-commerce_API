from sqlalchemy.orm import Mapped, mapped_column
from database import Base, db

class CustomerManagementRole(Base):
    __tablename__ = 'customer_management_roles'
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    customer_management_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('customer_accounts.id'))
    role_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('roles.id'))
