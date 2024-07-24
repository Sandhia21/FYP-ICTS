import requests
import time

BASE_URL = "http://127.0.0.1:8000/users/"

def test_register():
    endpoint = f"{BASE_URL}register/"
    unique_username = f"user_{int(time.time())}"
    data = {
        "username": unique_username,
        "email": f"{unique_username}@example.com",
        "password": "password123",
        "role": "student"
    }
    response = requests.post(endpoint, data=data)
    print(f"Registration Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

if __name__ == "__main__":
    test_register()