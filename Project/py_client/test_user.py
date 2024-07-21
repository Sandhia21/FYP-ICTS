import requests

BASE_URL = "http://127.0.0.1:8000/api/"

def test_create_user():
    endpoint = f"{BASE_URL}users/"
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123",
        "role": "student"
    }
    response = requests.post(endpoint, data=data)
    print(f"Create User Status Code: {response.status_code}")
    print(response.json())

def test_get_users():
    endpoint = f"{BASE_URL}users/"
    response = requests.get(endpoint)
    print(f"Get Users Status Code: {response.status_code}")
    print(response.json())

def test_get_user(user_id):
    endpoint = f"{BASE_URL}users/{user_id}/"
    response = requests.get(endpoint)
    print(f"Get User Status Code: {response.status_code}")
    print(response.json())

def test_update_user(user_id):
    endpoint = f"{BASE_URL}users/{user_id}/"
    data = {
        "email": "newemail@example.com"
    }
    response = requests.put(endpoint, data=data)
    print(f"Update User Status Code: {response.status_code}")
    print(response.json())

def test_delete_user(user_id):
    endpoint = f"{BASE_URL}users/{user_id}/"
    response = requests.delete(endpoint)
    print(f"Delete User Status Code: {response.status_code}")
    print(response.status_code)

if __name__ == "__main__":
    test_create_user()
    test_get_users()
    user_id = 1  # Change this to an existing user ID
    test_get_user(user_id)
    test_update_user(user_id)
    test_delete_user(user_id)