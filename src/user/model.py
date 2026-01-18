from pydantic import BaseModel

class register(BaseModel):
    email:str
    name:str
    role:str
    password:str

class Login(BaseModel):
    email: str
    password: str

class create_user(BaseModel):
    email:str
    name:str
    is_deleted:bool=False
    password:str
    role:str

class response_user(BaseModel):
    id:int
    name:str
    email:str
    role:str
    is_deleted:bool
    

class update_User(BaseModel):
    name: str
    is_deleted:bool
    password:str
    role:str