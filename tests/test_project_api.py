def test_get_project(client,auth_data,test_project):
    token=auth_data["token"]
    project_id=test_project["project_id"]
    response=client.get(f"/project/{project_id}",headers={"Authorization":f"Bearer {token}"})
    assert response.status_code==200

def test_get_all_projects(client,auth_data):
    token=auth_data["token"]
    response=client.get("/projects/",headers={"Authorization":f"Bearer {token}"})
    assert response.status_code==200

def test_update_project(client,auth_data,test_project):
    token=auth_data["token"]
    project_id=test_project["project_id"]
    update_project={ 
            "project_id": project_id,
            "project_name": "test_project_updated",
            "description":"project for testing",
            "owner_id": test_project["owner_id"],
            "status":"in_progress"
        }
    response=client.put(
        "/project/update/",
        json=update_project,
        headers={"Authorization":f"Bearer {token}"})
    assert response.status_code==200
    assert response.json() ["project_name"]=="test_project_updated"

def test_delete_project(client,auth_data,test_project):
    token=auth_data["token"]
    project_id=test_project["project_id"]
    response=client.delete(f"/project/delete/{project_id}",headers={"Authorization":f"Bearer {token}"})
    assert response.status_code==200
