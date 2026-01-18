from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from src.user.model import create_user, response_user, update_User,register
from src.user.service import Service
from auth import create_access_token
from dependencies import get_current_user
from typing import List

router = APIRouter(prefix="",tags=["Users"])

@router.post("/user/register", response_model=response_user)
def Register_user_api(
    user: register,
    db=Depends(get_db)
):
    try:
        result = Service.create_user(user, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db=Depends(get_db)
):
    # Swagger sends email as username
    db_user = Service.authenticate_user(
        form_data.username,
        form_data.password,
        db
    )
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": str(db_user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/user/create", response_model=response_user)
def create_user_api(
    user: create_user,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return Service.create_user(user, db)


@router.get("/user/{id}")
def get_user_by_id(
    id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        result = Service.get_user_by_id(id, db, current_user)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/users/",response_model=List[response_user])
def get_all_users(page:int=1,page_size:int=10,db=Depends(get_db),current_user=Depends(get_current_user)):
    result=Service.get_all_users(page,page_size,db)
    return result
    
@router.put("/user/{id}", response_model=response_user)
def update_user(
    id: int,
    user: update_User,
    db=Depends(get_db)
):
    return Service.update_user(id, user, db)

@router.delete("/user/{id}")
def delete_user(
    id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return Service.delete_user(id, db, current_user)