# Generated by Django 5.0.3 on 2024-05-09 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_course_professor_course_professor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CouserSelection',
            new_name='CourseSelection',
        ),
    ]