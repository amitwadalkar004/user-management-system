from fastapi import APIRouter, Depends,HTTPException
from database import get_db
from src.project.model import create_project,update_project,response_project
from src.project.service import project_service
from dependencies import get_current_user
from typing import List

router=APIRouter(prefix="", tags=["projects"])

@router.post("/project/create", response_model=response_project)
def create_project(
    project: create_project,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        result=project_service.create_project(project,current_user,db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/project/{project_id}")
def get_project(
    project_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        result=project_service.get_project(project_id,db)
        return result
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.get("/projects/",response_model=List[response_project])
def get_all_projects(page:int=1,page_size:int=10,db=Depends(get_db),current_user=Depends(get_current_user)):
    try:
        result=project_service.get_all_projects(page,page_size,db) 
        return result
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@router.put("/project/update/", response_model=response_project)
def update_project(update_project: update_project,current_user=Depends(get_current_user),db=Depends(get_db)):
    try:
        result=project_service.update_project(update_project,current_user,db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    

@router.delete("/project/delete/{project_id}")
def delete_project(project_id:int,db=Depends(get_db),current_user=Depends(get_current_user)):
    try:
        result=project_service.delete_project(project_id,db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))