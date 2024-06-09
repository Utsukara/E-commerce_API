from sqlalchemy.orm import Mapped, mapped_column
from database import Base, db

class Role(Base):
    __tablename__ = 'roles'
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    role_name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
