import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/course_model.dart';

class ApiService {
  final String baseUrl = 'http://127.0.0.1:8000/api';

  Future<List<Course>> fetchTeacherCourses() async {
    final response = await http.get(Uri.parse('$baseUrl/courses/'));

    if (response.statusCode == 200) {
      List<dynamic> data = json.decode(response.body);
      return data.map((course) => Course.fromJson(course)).toList();
    } else {
      throw Exception('Failed to load courses');
    }
  }

  Future<List<Course>> fetchStudentCourses() async {
    final response = await http.get(Uri.parse('$baseUrl/courses/'));

    if (response.statusCode == 200) {
      List<dynamic> data = json.decode(response.body);
      return data.map((course) => Course.fromJson(course)).toList();
    } else {
      throw Exception('Failed to load courses');
    }
  }

  Future<void> selfEnroll(String courseCode, String courseKey) async {
    final response = await http.post(
      Uri.parse('$baseUrl/courses/self_enroll/'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'course_code': courseCode, 'course_key': courseKey}),
    );

    if (response.statusCode != 201) {
      throw Exception('Failed to enroll in course');
    }
  }
}
