from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str:
        return self.username


class Major(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    student_number = models.CharField(max_length=20)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.user.username


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    prof_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=20)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    capacity = models.PositiveSmallIntegerField()
    unit = models.PositiveSmallIntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name}, {self.professor}"

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    time = models.TimeField()

    def __str__(self) -> str:
        return f"{self.course.name}, {self.course.professor.user.username}"


class CouserSelection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.PROTECT) 
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    place = models.CharField(max_length=20)
    time = models.TimeField()
