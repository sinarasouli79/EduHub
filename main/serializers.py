from django.conf import settings
from rest_framework import serializers

from .models import Course, CourseSelection, Major, Professor, Section, Student, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_staff",
            "is_active",
        )


class ProfessorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Professor
        fields = ("id", "user", "prof_number")


class CourseSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer()

    class Meta:
        model = Course
        fields = ("id", "name", "major", "capacity", "unit", "professor")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class CouseSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSelection
        fields = "__all__"


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = "__all__"
