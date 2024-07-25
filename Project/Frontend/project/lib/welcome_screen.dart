import 'package:flutter/material.dart';
import 'package:project/user_viewmodel.dart';
import 'package:provider/provider.dart';
import 'login_screen.dart';

class WelcomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Welcome'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              onPressed: () {
                Provider.of<UserViewModel>(context, listen: false)
                    .setUserRole('Teacher');
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => LoginScreen()),
                );
              },
              child: Text('I am a Teacher'),
            ),
            ElevatedButton(
              onPressed: () {
                Provider.of<UserViewModel>(context, listen: false)
                    .setUserRole('Student');
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => LoginScreen()),
                );
              },
              child: Text('I am a Student'),
            ),
          ],
        ),
      ),
    );
  }
}
