import requests

base_url = "http://127.0.0.1:8000/api"
auth_token_admin = "2bb53572ae208ef644b5881e93aff261cfd2a3ba"  # Replace with a valid admin token
auth_token_student = "cf21c844d2810c4be74a4e3da0490affa3281b56"  # Replace with a valid student token

headers_admin = {'Authorization': f'Token {auth_token_admin}'}
headers_student = {'Authorization': f'Token {auth_token_student}'}

# Step 1: Create a new course
course_data = {
    "name": "Self Enrollment Course",
    "code": "SELFENR02",
    "description": "Course for testing self enrollment",
    "teacher": 1
}

response = requests.post(f"{base_url}/courses/", headers=headers_admin, json=course_data)
print("Create Course Status Code:", response.status_code)
if response.status_code != 201:
    print("Failed to create course")
    print(response.json())
    exit()

course = response.json()
print(course)
course_id = course['id']
course_code = course['code']
course_key = course['course_key']

# Step 2: Self-enroll in the course
print(f"Attempting self-enroll with course_code: {course_code} and course_key: {course_key}")

self_enroll_data = {
    "course_code": course_code,
    "course_key": course_key
}

response = requests.post(f"{base_url}/courses/self-enroll/", headers=headers_student, json=self_enroll_data)
print("Self Enroll Status Code:", response.status_code)
print(response.json())

# Step 3: Clean up by deleting the created course
delete_response = requests.delete(f"{base_url}/courses/{course_id}/", headers=headers_admin)
print("Delete Course Status Code:", delete_response.status_code)
