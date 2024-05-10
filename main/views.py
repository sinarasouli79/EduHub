from rest_framework import viewsets

from .models import Course, CourseSelection, Major, Professor, Section, Student
from .serializers import (
    CourseSerializer,
    CouseSelectionSerializer,
    MajorSerializer,
    ProfessorSerializer,
    SectionSerializer,
    StudentSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = (
        Course.objects.select_related("professor__user")
        .prefetch_related("section_set")
        .all()
    )
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class CourseSelectionViewSet(viewsets.ModelViewSet):
    queryset = CourseSelection.objects.all()
    serializer_class = CouseSelectionSerializer


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
