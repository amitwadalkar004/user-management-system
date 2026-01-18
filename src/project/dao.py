from src.project.schema import Project
from logger import get_logger

logger=get_logger()

class project_dao:
    
    @staticmethod
    def create_project(project,db):
        result=Project(**project.model_dump())
        db.add(result)
        db.flush()
        return result

    @staticmethod
    def get_project(project_id,db):
        try:
            result=db.query(Project).filter(Project.project_id==project_id).first()
            if not result:
                raise Exception("Project not found")
            logger.info("project fetch successfully")
            return result
        except Exception as e:
            raise e

    @staticmethod
    def get_all_projects(skip,limit,db):
        try:
            # .offset() skips the first N items
            # .limit() restricts the number of items returned
            result = db.query(Project).offset(skip).limit(limit).all()
            return result
        except Exception as e:
            raise e

    @staticmethod
    def update_project(update_project,db):
        try:
            project=db.query(Project).filter(Project.project_id==update_project.project_id).first()
            if project:          
                project.project_name=update_project.project_name
                project.description=update_project.description
                project.owner_id=update_project.owner_id  
            else:
                raise Exception("Project not found")  
            db.commit()
            db.refresh(project)
            return project
        except Exception as e:
            raise e    

    @staticmethod
    def delete_project(project_id,db):
        try:
            result=db.query(Project).filter(Project.project_id==project_id).update({"is_deleted":True})
            db.commit()
            return {result:"project deleted successfully"}
        except Exception as e:
            raise e
