import requests

BASE_URL = "http://127.0.0.1:8000/api/"

def test_create_enrollment():
    endpoint = f"{BASE_URL}enrollments/"
    data = {
        "student": 1,  # Change this to a valid student user ID
        "course": 1  # Change this to a valid course ID
    }
    response = requests.post(endpoint, data=data)
    print(f"Create Enrollment Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

def test_get_enrollments():
    endpoint = f"{BASE_URL}enrollments/"
    response = requests.get(endpoint)
    print(f"Get Enrollments Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

def test_get_enrollment(enrollment_id):
    endpoint = f"{BASE_URL}enrollments/{enrollment_id}/"
    response = requests.get(endpoint)
    print(f"Get Enrollment Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

def test_update_enrollment(enrollment_id):
    endpoint = f"{BASE_URL}enrollments/{enrollment_id}/"
    data = {
        "course": 2  # Change this to a new valid course ID
    }
    response = requests.put(endpoint, data=data)
    print(f"Update Enrollment Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

def test_delete_enrollment(enrollment_id):
    endpoint = f"{BASE_URL}enrollments/{enrollment_id}/"
    response = requests.delete(endpoint)
    print(f"Delete Enrollment Status Code: {response.status_code}")

if __name__ == "__main__":
    test_create_enrollment()
    test_get_enrollments()
    enrollment_id = 1  # Change this to an existing enrollment ID
    test_get_enrollment(enrollment_id)
    test_update_enrollment(enrollment_id)
    test_delete_enrollment(enrollment_id)