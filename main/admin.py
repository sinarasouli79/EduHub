from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import Course, CourseSelection, Major, Professor, Section, Student, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin): ...


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin): ...


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        return qs.select_related("user")


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        return qs.select_related("user")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        return qs.select_related("professor__user")


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin): ...


@admin.register(CourseSelection)
class CouserCouserSelection(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        return qs.select_related(
            "student__user", "section__course", "section__course__professor__user"
        )
