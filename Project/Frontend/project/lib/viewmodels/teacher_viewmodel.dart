import 'package:flutter/material.dart';
import '../models/course_model.dart';
import '../services/api_service.dart';

class TeacherViewModel extends ChangeNotifier {
  List<Course> _courses = [];
  bool _isLoading = false;

  List<Course> get courses => _courses;
  bool get isLoading => _isLoading;

  Future<void> fetchCourses() async {
    _isLoading = true;
    notifyListeners();

    _courses = await ApiService().fetchTeacherCourses();

    _isLoading = false;
    notifyListeners();
  }
}
