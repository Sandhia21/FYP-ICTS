class Course {
  final String id;
  final String name;
  final String code;
  final String description;
  final String teacher;
  final String courseKey;

  Course(
      {required this.id,
      required this.name,
      required this.code,
      required this.description,
      required this.teacher,
      required this.courseKey});

  factory Course.fromJson(Map<String, dynamic> json) {
    return Course(
      id: json['id'],
      name: json['name'],
      code: json['code'],
      description: json['description'],
      teacher: json['teacher'],
      courseKey: json['course_key'],
    );
  }
}
