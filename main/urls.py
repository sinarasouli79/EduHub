from rest_framework import routers

from .views import (
    CourseSelectionViewSet,
    CourseViewSet,
    MajorViewSet,
    ProfessorViewSet,
    SectionViewSet,
    StudentViewSet,
)

router = routers.DefaultRouter()
router.register("courses", CourseViewSet)
router.register("student", StudentViewSet)
router.register("professor", ProfessorViewSet)
router.register("section", SectionViewSet)
router.register("course-selection", CourseSelectionViewSet)
router.register("major", MajorViewSet)
urlpatterns = router.urls
