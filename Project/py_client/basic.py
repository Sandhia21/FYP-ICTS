# import requests

# BASE_URL = "http://127.0.0.1:8000/users/"

# def test_login():
#     endpoint = f"{BASE_URL}login/"
#     data = {
#         "username": "newuser",
#         "password": "newpassword123"
#     }
#     response = requests.post(endpoint, data=data)
#     print(f"Login Status Code: {response.status_code}")
#     try:
#         print(response.json())
#     except requests.exceptions.JSONDecodeError:
#         print("Response content is not in JSON format")
#         # print(response.text)

# if __name__ == "__main__":
#     test_login()



# import requests

# BASE_URL = "http://127.0.0.1:8000/users/"

# def test_registration():
#     endpoint = f"{BASE_URL}register/"
#     data = {
#         "username": "newuser",
#         "email": "newuser@example.com",
#         "password": "newpassword123",
#         "role": "student"
#     }
#     response = requests.post(endpoint, data=data)
#     print(f"Registration Status Code: {response.status_code}")
#     try:
#         print(response.json())
#     except requests.exceptions.JSONDecodeError:
#         print("Response content is not in JSON format")
#         print(response.text)

# if __name__ == "__main__":
#     test_registration()
import requests

BASE_URL = "http://127.0.0.1:8000/users/"

def test_login():
    endpoint = f"{BASE_URL}login/"
    data = {
        "username": "newuser",
        "password": "newpassword123"
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