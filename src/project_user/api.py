from fastapi import APIRouter,Depends,HTTPException
from src.project_user.model import project_user
from dependencies import get_current_user
from database import get_db
from src.project_user.service import project_user_service

router=APIRouter(prefix="",tags=["project_user"])

@router.post("/project_user/",response_model=project_user)
def add_project_user(projectuser:project_user,current_user=Depends(get_current_user),db=Depends(get_db)): 
    result=project_user_service.add_project_user(projectuser,current_user,db)
    return result


@router.get("/project/users/{project_id}")
def get_project_users(project_id,current_user=Depends(get_current_user),db=Depends(get_db)):
    result=project_user_service.get_project_users(project_id,current_user,db)
    return result
    
    
@router.get("/user/projects/{user_id}")
def get_user_projects(user_id,db=Depends(get_db),current_user=Depends(get_current_user)):
    result=project_user_service.get_user_projects(user_id,current_user,db)
    return result
    

@router.delete("/project_user/{user_id}")
def delete_project_user(user_id,db=Depends(get_db),current_user=Depends(get_current_user)):
    result=project_user_service.delete_project_user(user_id,current_user,db)
    return result




