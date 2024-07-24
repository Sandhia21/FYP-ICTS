import requests

BASE_URL = "http://127.0.0.1:8000/users/"

def test_login():
    endpoint = f"{BASE_URL}login/"
    data = {
        "username": "uniqueuser123",
        "password": "password123"
    }
    response = requests.post(endpoint, data=data)
    print(f"Login Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

if __name__ == "__main__":
    test_login()