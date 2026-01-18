from pydantic import BaseModel

class create_project(BaseModel):
    project_name: str
    description:str
    owner_id: int
    status:str

class response_project(BaseModel):
    project_id: int
    project_name: str
    description:str
    owner_id: int
    status:str

class update_project(BaseModel):
    project_id: int
    project_name: str
    description:str
    owner_id: int
    status:str

