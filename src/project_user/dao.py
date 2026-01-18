from src.project_user.schema import project_user
from src.user.schema import User
from src.project.schema import Project
from logger import get_logger

logger=get_logger()

class project_user_dao:

    @staticmethod
    def add_project_user(projectuser,db):
        result=project_user(**projectuser.model_dump())
        db.add(result)
        db.commit()
        return result

        
    @staticmethod
    def get_project_users(project_id,db):
        result=db.query(User.name.label("username"),User.role,Project.project_name.label("project_name"),project_user.is_deleted).select_from(project_user).join(User,User.id==project_user.user_id).join(Project,project_user.project_id==Project.project_id).filter(project_user.project_id==project_id,project_user.is_deleted==False).all()
        if not result:
            raise Exception("user not found for this project")
        logger.info("user fetch successfully")
        return [
    {
        "username": row.username,
        "role": row.role,
        "project_name": row.project_name,
        "is_deleted": row.is_deleted
    }
    for row in result
]
        
        
    @staticmethod
    def get_user_projects(user_id,db):
        result = (
            db.query(
                Project.project_name,
                Project.description,
                Project.is_deleted,
                project_user.role
            )
            .select_from(project_user)
            .join(Project, Project.project_id == project_user.project_id)
            .filter(
                project_user.user_id == user_id,
                project_user.is_deleted==False
            )
            .all()
        )
        if not result:
            raise Exception("No projects for this user")
        logger.info("result in dao")
        return [
    {
        "project_name": row.project_name,
        "description":row.description,
        "is_deleted": row.is_deleted,
        "role":row.role
    }
    for row in result
]
        
        
    @staticmethod
    def delete_project_user(user_id,db):
        result=db.query(project_user).filter(project_user.user_id==user_id).update({"is_deleted":True})
        db.commit()
        return {result : "project_user deleted successfully"}
        