// import 'package:flutter/material.dart';
// import '../../models/course_model.dart';

// class TeacherCourseView extends StatelessWidget {
//   final Course course;

//   TeacherCourseView({required this.course});

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text(course.name),
//       ),
//       body: Padding(
//         padding: const EdgeInsets.all(16.0),
//         child: Column(
//           crossAxisAlignment: CrossAxisAlignment.start,
//           children: [
//             Text(
//               course.description,
//               style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
//             ),
//             SizedBox(height: 20),
//             Expanded(
//               child: ListView.builder(
//                 itemCount: course.tableOfContents.length,
//                 itemBuilder: (context, index) {
//                   final toc = course.tableOfContents[index];
//                   return ListTile(
//                     title: Text(toc.title),
//                     subtitle: Text(
//                         'Contains ${toc.notes.length} notes and ${toc.quizzes.length} quizzes'),
//                   );
//                 },
//               ),
//             ),
//           ],
//         ),
//       ),
//       floatingActionButton: FloatingActionButton(
//         onPressed: () {
//           // Handle adding new table of content
//         },
//         child: Icon(Icons.add),
//       ),
//     );
//   }
// }
