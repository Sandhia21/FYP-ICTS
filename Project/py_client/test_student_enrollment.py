import requests

BASE_URL = "http://127.0.0.1:8000/api/"

def get_tokens():
    with open("tokens.txt", "r") as file:
        tokens = file.readlines()
    return tokens[0].strip().split(": ")[1], tokens[1].strip().split(": ")[1]

def self_enroll(token, course_code, course_key):
    endpoint = f"{BASE_URL}courses/self_enroll/"
    headers = {'Authorization': f'Token {token}'}
    data = {"course_code": course_code, "course_key": course_key}
    response = requests.post(endpoint, headers=headers, data=data)
    print(f"Self Enroll Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")

def exit_course(token, course_id):
    endpoint = f"{BASE_URL}enrollments/{course_id}/exit/"
    headers = {'Authorization': f'Token {token}'}
    response = requests.post(endpoint, headers=headers)
    print(f"Exit Course Status Code: {response.status_code}")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response content is not in JSON format")

if __name__ == "__main__":
    teacher_token, student_token = get_tokens()

    # Student self enrolls in a course
    self_enroll(student_token, "TC101", "course_key_here")

    # Student exits the course
    exit_course(student_token, 1)  # Assuming course ID is 1