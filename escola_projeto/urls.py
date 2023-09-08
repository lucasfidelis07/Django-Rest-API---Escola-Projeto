from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/', include('alunos.urls')),
    path('api/cursos/', include('cursos.urls')),
]