def test_add_project_user(client,auth_data,test_project):
    token=auth_data["token"]
    project_id=test_project["project_id"]
    user_id=auth_data["user_id"]
    payload={
        "project_id":project_id,
        "user_id": user_id,
        "role":"ADMIN",
        "is_deleted":False
    }

    response=client.post("/project_user/",json=payload,headers={"Authorization":f"Bearer {token}"})
    if response.status_code !=200:
        print(f"Error detail : {response.json()}")
    assert response.status_code==200

def test_get_project_users(client,auth_data,test_project):
    token=auth_data["token"]
    project_id=test_project["project_id"]
    response=client.get(f"/project/users/{project_id}",headers={"Authorization":f"Bearer {token}"})
    assert response.status_code==200

def test_get_user_projects(client,auth_data):
    token=auth_data["token"]
    user_id=auth_data["user_id"]
    response=client.get(f"/user/projects/{user_id}",headers={"Authorization": f"Bearer {token}"})
    assert response.status_code==200


def test_delete_project_user(client,auth_data):
    token=auth_data["token"]
    user_id=auth_data["user_id"]
    response=client.delete(f"/project_user/{user_id}",headers={"Authorization": f"Bearer {token}"})
    assert response.status_code==200