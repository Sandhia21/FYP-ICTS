import 'package:flutter/material.dart';
import '../models/course_model.dart';
import '../services/api_service.dart';

class StudentViewModel extends ChangeNotifier {
  List<Course> _courses = [];
  bool _isLoading = false;

  List<Course> get courses => _courses;
  bool get isLoading => _isLoading;

  Future<void> fetchCourses() async {
    _isLoading = true;
    notifyListeners();

    _courses = await ApiService().fetchStudentCourses();

    _isLoading = false;
    notifyListeners();
  }

  Future<void> enrollInCourse(String courseCode, String courseKey) async {
    _isLoading = true;
    notifyListeners();

    await ApiService().selfEnroll(courseCode, courseKey);

    await fetchCourses();
  }
}
