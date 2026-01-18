from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from database import Base, engine
from src.project.schema import Project
from src.user.schema import User

class project_user(Base):
    __tablename__='project_user'
    id=Column(Integer, primary_key=True)
    project_id=Column(Integer, ForeignKey('projects.project_id'))
    user_id=Column(Integer, ForeignKey('users_new.id'))
    role=Column(String,nullable=False)
    is_deleted=Column(Boolean)

Base.metadata.create_all(bind=engine)