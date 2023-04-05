from .databases import Base
from sqlalchemy import Column,String,Integer,TIMESTAMP,text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    full_name = Column(String,nullable=False)
    address = Column(String,nullable=False)
    birth_day = Column(TIMESTAMP(),nullable=False)
    gender = Column(String,nullable=False)
    image = Column(String,nullable=True)
    create_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
