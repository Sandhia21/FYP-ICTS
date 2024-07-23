import requests
import uuid

BASE_URL = "http://127.0.0.1:8000/api/"

def test_create_course():
    endpoint = f"{BASE_URL}courses/"
    unique_code = f"TC{uuid.uuid4().hex[:6]}"  # Generate a unique course code
    data = {
        "name": "Test Course",
        "code": unique_code,
        "description": "This is a test course.",
        "teacher": 1  # Change this to a valid teacher user ID
    }
    response = requests.post(endpoint, data=data)
    print(f"Create Course Status Code: {response.status_code}")
    try:
        print(response.json())
        return response.json().get('id')  # Return the created course ID
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)
        return None

def test_get_courses():
    endpoint = f"{BASE_URL}courses/"
    response = requests.get(endpoint)
    print(f"Get Courses Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

def test_get_course(course_id):
    endpoint = f"{BASE_URL}courses/{course_id}/"
    response = requests.get(endpoint)
    print(f"Get Course Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

def test_update_course(course_id):
    endpoint = f"{BASE_URL}courses/{course_id}/"
    data = {
        "name": "Updated Course Name",
        "code": "TC101",  # Use the same code
        "description": "Updated course description.",
        "teacher": 1  # Make sure to include all required fields
    }
    response = requests.put(endpoint, data=data)
    print(f"Update Course Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")
        print(response.text)

def test_delete_course(course_id):
    endpoint = f"{BASE_URL}courses/{course_id}/"
    response = requests.delete(endpoint)
    print(f"Delete Course Status Code: {response.status_code}")

if __name__ == "__main__":
    created_course_id = test_create_course()
    if created_course_id:
        test_get_courses()
        test_get_course(created_course_id)
        test_update_course(created_course_id)
        test_delete_course(created_course_id)
    else:
        print("Course creation failed, skipping further tests.")