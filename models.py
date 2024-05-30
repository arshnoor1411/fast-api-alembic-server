from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False)
    firstname = Column(String,nullable=False)
    lastname = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), onupdate = func.now())
    deleted_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
