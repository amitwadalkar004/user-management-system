from fastapi import FastAPI
from src.user.api import router as user_router
from src.project.api import router as project_router
from src.project_user.api import router as project_user_router
app = FastAPI()

app.include_router(user_router)
app.include_router(project_router)
app.include_router(project_user_router)
