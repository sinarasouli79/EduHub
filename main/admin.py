from django.contrib import admin

from .models import Course, CouserSelection, Major, Professor, Section, Student, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin): ...


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin): ...


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin): ...


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin): ...


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): ...


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin): ...


@admin.register(CouserSelection)
class CouserCouserSelection(admin.ModelAdmin): ...
