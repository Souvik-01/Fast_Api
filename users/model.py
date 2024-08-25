from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from datetime import datetime

from core.database import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20), nullable=True)
    email = Column(String(20), unique=True, index=True)
    password = Column(String(100))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    photo = Column(String(30), nullable=True)
    updated_at = Column(DateTime, nullable=True)
