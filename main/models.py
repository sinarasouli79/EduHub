from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.username}"


class Major(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    student_number = models.CharField(max_length=20)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.user.username}"


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    prof_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.user.username}"


class Course(models.Model):
    name = models.CharField(max_length=20)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    capacity = models.PositiveSmallIntegerField()
    unit = models.PositiveSmallIntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name}, {self.professor.user.username}"


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    time = models.TimeField()

    def __str__(self) -> str:
        return f"{self.course.professor.user.username}, {self.course.name}-{self.time}"


class CourseSelection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    place = models.CharField(max_length=20)
    time = models.TimeField()

    def __str__(self) -> str:
        return f"{self.student.user.username}, {self.section.course.name}-{self.section.time}"
