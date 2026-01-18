from pydantic import BaseModel, Field

class project_user(BaseModel):
    project_id: int=Field(..., description="ID of the project")
    user_id: int=Field(...,description="ID of the user")
    role:str
    is_deleted:bool
