from fastapi import HTTPException
from src.project.dao import project_dao
from logger import get_logger
from src.rbac import check_project_permission
from src.project_user.service import project_user_service
from src.project_user.model import project_user
import math

logger=get_logger()

class project_service:
    @staticmethod
    def create_project(project,current_user,db):
        try:
            result=project_dao.create_project(project,db)

            projectuser=project_user_service.add_project_user(
              project_user(
                project_id=result.project_id,
                user_id=current_user.id,
                role="OWNER",
                is_deleted=False
                ),
                current_user,
                db,
                skip_permission=True
                )          
            db.commit()

            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def get_project(project_id,db):
        try:
            result=project_dao.get_project(project_id,db)
            return result
        except Exception as e:
            raise e

    @staticmethod
    def get_all_projects(page,page_size,db):
        try:
            page = (page - 1) * page_size
            result=project_dao.get_all_projects(page,page_size,db)
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def update_project(update_project,current_user,db):
        try:
            check_project_permission(
                db=db,
                user_id=current_user.id,
                project_id=update_project.project_id,
                required_permission="update_project"      
            )
            result=project_dao.update_project(update_project,db)
            return result
        except Exception as e:
            raise e
        

    @staticmethod
    def delete_project(project_id,db):
        try:
            result=project_dao.delete_project(project_id,db)
            return result
        except Exception as e:
            raise e