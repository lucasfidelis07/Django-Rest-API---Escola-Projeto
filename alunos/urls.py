from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, DisciplinaViewSet, NotaViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]