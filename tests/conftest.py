import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from database import Base
from database import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    return TestClient(app)




@pytest.fixture
def auth_data(client):
    user_payload = {
        "email": "test20@example.com",
        "name": "xyz",
        "role": "ADMIN", 
        "password": "password123"
    }

    # 1. Register
    reg_resp = client.post("/user/register", json=user_payload)
    
    # 2. Login (Always do this to get a fresh token)
    login_resp = client.post(
        "/login", 
        data={"username": user_payload["email"], "password": user_payload["password"]}
    )
    
    if login_resp.status_code != 200:
        raise Exception(f"Login failed: {login_resp.json()}")

    if reg_resp.status_code in [200, 201]:
        user_id = reg_resp.json()["id"]
    else:
        me_resp = client.get(
            "/users/me", 
            headers={"Authorization": f"Bearer {login_resp.json()['access_token']}"}
        )
        user_id = me_resp.json()["id"]
    
    return {
        "token": login_resp.json()["access_token"],
        "user_id": user_id
    }



@pytest.fixture
def test_user(client):
    """Creates a user and returns the user object (including ID)"""
    response = client.post(
        "/user/register",
        json={
            "email": "fixture_user@example.com",
            "name": "Fixture User",
            "role": "ADMIN",
            "password": "password123"
        }
    )
    # Return the dictionary containing 'id', 'email', etc.
    return response.json()

@pytest.fixture
def test_project(client,auth_data):
    """ Creates a project and return the project object"""
    token=auth_data["token"]
    response=client.post(
        "/project/create",
        json={
            "project_name": "test_project",
            "description":"project for testing",
            "owner_id": auth_data["user_id"],
            "status":"in_progress"
        },
        headers={"Authorization":f"Bearer {token}"}
    )
    return response.json()

@pytest.fixture
def test_project_user(client, auth_data, test_project):
    """Links the user to the project so they have permission to update it"""
    token=auth_data["token"]
    response = client.post(
        "/project_user/",
        json={
            "project_id": test_project["project_id"],
            "user_id": auth_data["user_id"],
            "role": "OWNER", # OWNER has "update_project" permission in your dict
            "is_deleted": False
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()


@pytest.fixture(scope="function")
def client():
    # 1. Force a clean schema BEFORE creating the client
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    with TestClient(app) as c:
        yield c
    
    # 2. Clean up after the test is done (optional)
    Base.metadata.drop_all(bind=engine)


# @pytest.fixture(autouse=True)
# def run_around_tests():
#     # Setup: Clean database before test
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     yield
    # Teardown: (Optional) logic after test

