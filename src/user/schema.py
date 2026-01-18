from sqlalchemy import Column, Integer, String,Boolean
from database import Base,engine

class User(Base):
    __tablename__="users_new"
    id=Column(Integer, primary_key=True, index=True)
    email=Column(String)
    name= Column(String)
    is_deleted=Column(Boolean, default=False)
    password = Column(String, nullable=False)
    role=Column(String)

Base.metadata.create_all(bind=engine)
# print("Tables Created Successfully")