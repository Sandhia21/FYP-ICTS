import requests

BASE_URL = "http://127.0.0.1:8000/users/"

def test_register_user(username, email, password, role):
    endpoint = f"{BASE_URL}register/"
    data = {
        "username": username,
        "email": email,
        "password": password,
        "role": role
    }
    response = requests.post(endpoint, data=data)
    print(f"Registration Status Code for {username}: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")

def test_login_user(username, password):
    endpoint = f"{BASE_URL}login/"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(endpoint, data=data)
    print(f"Login Status Code for {username}: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
    return response.json().get('token')

if __name__ == "__main__":
    # Register a student
    test_register_user("student1", "student1@example.com", "password123", "student")
    # Register a teacher
    test_register_user("teacher1", "teacher1@example.com", "password123", "teacher")

    # Login with the student
    student_token = test_login_user("student1", "password123")
    # Login with the teacher
    teacher_token = test_login_user("teacher1", "password123")