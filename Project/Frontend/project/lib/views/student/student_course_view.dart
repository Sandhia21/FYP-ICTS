// import 'package:flutter/material.dart';
// import '../../models/course_model.dart';
// import '../../viewmodels/student_viewmodel.dart';
// import 'package:provider/provider.dart';

// class StudentCourseView extends StatelessWidget {
//   final Course course;

//   StudentCourseView({Key? key, required this.course}) : super(key: key);

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
//               style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
//             ),
//             const SizedBox(height: 20),
//             Expanded(
//               child: ListView.builder(
//                 itemCount: course.tableOfContents.length,
//                 itemBuilder: (context, index) {
//                   final toc = course.tableOfContents[index];
//                   return ListTile(
//                     title: Text(toc.title),
//                     subtitle: Text(
//                         'Contains ${toc.notes.length} notes and ${toc.quizzes.length} quizzes'),
//                     onTap: () {
//                       // Handle viewing notes and quizzes
//                     },
//                   );
//                 },
//               ),
//             ),
//           ],
//         ),
//       ),
//       floatingActionButton: FloatingActionButton(
//         onPressed: () {
//           // Handle enrolling in the course
//         },
//         child: const Icon(Icons.add),
//       ),
//     );
//   }
// }
