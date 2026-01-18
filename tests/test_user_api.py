def test_login_user(client):
    # 1. SETUP: Create the user so they exist in 'test.db'
    # Use the same credentials you will use for login
    client.post(
        "/user/register", 
        json={
            "email": "test20@example.com",
            "name": "xyz",
            "role": "MEMBER",
            "password": "password123"
        }
    )

    # 2. ACT: Try to login with the credentials we just created
    response = client.post(
        "/login",
        data={
            "grant_type": "password",
            "username": "test20@example.com",
            "password": "password123"
        }
    )
    # 3. ASSERT: This should now be 200
    assert response.status_code == 200
    assert "access_token" in response.json()



def test_create_user(client,auth_data):
    token=auth_data["token"]
    response = client.post(
        "/user/create",
        json={
            "email": "test200@example.com",
            "name": "xyz",
            "is_deleted": False,
            "password": "password123",
            "role": "abc"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200



def test_get_user_by_id(client,auth_data,test_user):
    token=auth_data["token"]
    user_id=test_user["id"]
    response=client.get(f"/user/{user_id}",headers={"Authorization":f"Bearer {token}"})
    assert response.status_code==200


def test_get_all_users(client,auth_data):
    token=auth_data["token"]
    response=client.get("/users/",headers={"Authorization":f"Bearer {token}"})
    assert response.status_code==200


def test_update_user(client, auth_data,test_user):
    token=auth_data["token"]
    user_id=test_user["id"]
    update_data = {
        "name": "Updated Name",
        "is_deleted": False,
        "password": "newpassword123",
        "role": "ADMIN"
    }
    # 3. Combine them in the request
    response = client.put(
        f"/user/{user_id}",           # Path Parameter goes here
        json=update_data,             # JSON Body goes here
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"


def test_delete_user(client,auth_data,test_user):
    token=auth_data["token"]
    user_id=test_user["id"]
    response=client.delete(f"/user/{user_id}", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code==200