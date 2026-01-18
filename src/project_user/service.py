from src.project_user.dao import project_user_dao
from fastapi import HTTPException
from src.rbac import check_project_permission
from logger import get_logger

logger=get_logger()

class project_user_service:
    
    @staticmethod
    def add_project_user(projectuser,current_user,db,skip_permission=False):
        if not skip_permission:
            check_project_permission(
                db=db,
                user_id=current_user.id,
                project_id=projectuser.project_id,
                required_permission="add_user"
            )            
        result=project_user_dao.add_project_user(projectuser,db)
        return result
    
        
    @staticmethod
    def get_project_users(project_id,current_user,db):
        check_project_permission(
            db=db,
            user_id=current_user.id,
            project_id=project_id,
            required_permission="view_user"
        )
        try:
            result=project_user_dao.get_project_users(project_id,db)
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def get_user_projects(user_id,current_user,db):
        logger.info(current_user)
        allowed_roles = ["ADMIN", "OWNER"]
    
        if current_user.id == user_id or current_user.role in allowed_roles:
        # 2. Logic: Return the mapping
            result= project_user_dao.get_user_projects(user_id, db)
            logger.info("result in service")
            return result
    
        
    @staticmethod
    def delete_project_user(user_id,current_user,db):
        allowed_roles = ["ADMIN", "OWNER"]    
        if current_user.id == user_id or current_user.role in allowed_roles:
            result=project_user_dao.delete_project_user(user_id,db)
            return result
        