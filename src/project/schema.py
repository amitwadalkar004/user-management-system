from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from database import Base,engine

class Project(Base):
    __tablename__="projects"
    project_id=Column(Integer, primary_key=True, index=True)
    project_name= Column(String, unique=True, index=True)
    owner_id=Column(Integer, ForeignKey("users_new.id"))
    description=Column(String)
    is_deleted=Column(Boolean,default=False)
    status=Column(String)

Base.metadata.create_all(bind=engine)