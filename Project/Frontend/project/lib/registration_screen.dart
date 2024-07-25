import 'package:flutter/material.dart';
import 'package:project/user_viewmodel.dart';
import 'package:project/views/student/student_dashboard.dart';
import 'package:project/views/teacher/teacher_dashboard.dart';
import 'package:provider/provider.dart';

class RegistrationScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Registration'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: <Widget>[
            TextField(
              decoration: InputDecoration(labelText: 'Email'),
            ),
            TextField(
              decoration: InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            TextField(
              decoration: InputDecoration(labelText: 'Confirm Password'),
              obscureText: true,
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Handle registration logic
                String role =
                    Provider.of<UserViewModel>(context, listen: false).userRole;
                if (role == 'Teacher') {
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(builder: (context) => TeacherDashboard()),
                  );
                } else {
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(builder: (context) => StudentDashboard()),
                  );
                }
              },
              child: Text('Register'),
            ),
          ],
        ),
      ),
    );
  }
}
