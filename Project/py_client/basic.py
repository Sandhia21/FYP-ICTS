import requests

BASE_URL = "http://127.0.0.1:8000"

def register(username, email, password, role):
    endpoint = f"{BASE_URL}/users/register/"
    data = {
        "username": username,
        "email": email,
        "password": password,
        "role": role
    }
    response = requests.post(endpoint, data=data)
    print(f"Registration Status Code: {response.status_code}")
    print(response.json())
    return response

def login(username, password):
    endpoint = f"{BASE_URL}/users/login/"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(endpoint, data=data)
    print(f"Login Status Code: {response.status_code}")
    print(response.json())
    result = response.json()
    return result.get('token', None)

teacher_token = login("teacher_username", "teacher_password")
student_token = login("student_username", "student_password")