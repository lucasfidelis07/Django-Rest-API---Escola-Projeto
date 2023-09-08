from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, TurmaViewSet

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'turmas', TurmaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]