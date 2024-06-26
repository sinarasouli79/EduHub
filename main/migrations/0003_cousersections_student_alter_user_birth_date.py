# Generated by Django 5.0.3 on 2024-05-02 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_course_major_user_birth_date_cousersections_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cousersections',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
