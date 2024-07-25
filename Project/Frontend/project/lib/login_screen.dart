import 'package:flutter/material.dart';
import 'package:project/registration_screen.dart';
import 'package:project/user_viewmodel.dart';
import 'package:project/views/student/student_dashboard.dart';
import 'package:project/views/teacher/teacher_dashboard.dart';
import 'package:provider/provider.dart';

class LoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Login'),
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
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Handle login logic
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
              child: Text('Login'),
            ),
            TextButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => RegistrationScreen()),
                );
              },
              child: Text("Don't have an account? Create Account"),
            ),
          ],
        ),
      ),
    );
  }
}
