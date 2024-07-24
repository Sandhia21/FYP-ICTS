from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_course_course_key_enrollment_date_enrolled_and_more'),  # Replace with the actual previous migration file name
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]