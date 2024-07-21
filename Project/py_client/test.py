import requests

BASE_URL = "http://127.0.0.1:8000/users/"

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
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        # print(response.text)

if __name__ == "__main__":
    test_create_user()