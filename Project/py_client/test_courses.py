import requests

BASE_URL = "http://127.0.0.1:8000/api/"

def test_create_course():
    endpoint = f"{BASE_URL}courses/"
    data = {
        "name": "Test Course",
        "code": "TC101",
        "description": "This is a test course.",
        "teacher": 1  # Change this to a valid teacher user ID
    }
    response = requests.post(endpoint, data=data)
    print(f"Create Course Status Code: {response.status_code}")
    print(response.json())

def test_get_courses():
    endpoint = f"{BASE_URL}courses/"
    response = requests.get(endpoint)
    print(f"Get Courses Status Code: {response.status_code}")
    print(response.json())

def test_get_course(course_id):
    endpoint = f"{BASE_URL}courses/{course_id}/"
    response = requests.get(endpoint)
    print(f"Get Course Status Code: {response.status_code}")
    print(response.json())

def test_update_course(course_id):
    endpoint = f"{BASE_URL}courses/{course_id}/"
    data = {
        "description": "Updated course description."
    }
    response = requests.put(endpoint, data=data)
    print(f"Update Course Status Code: {response.status_code}")
    print(response.json())

def test_delete_course(course_id):
    endpoint = f"{BASE_URL}courses/{course_id}/"
    response = requests.delete(endpoint)
    print(f"Delete Course Status Code: {response.status_code}")
    print(response.status_code)

if __name__ == "__main__":
    test_create_course()
    test_get_courses()
    course_id = 1  # Change this to an existing course ID
    test_get_course(course_id)
    test_update_course(course_id)
    test_delete_course(course_id)