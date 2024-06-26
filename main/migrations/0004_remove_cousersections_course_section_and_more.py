# Generated by Django 5.0.3 on 2024-05-02 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cousersections_student_alter_user_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cousersections',
            name='course',
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.course')),
            ],
        ),
        migrations.AddField(
            model_name='cousersections',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.section'),
            preserve_default=False,
        ),
    ]
