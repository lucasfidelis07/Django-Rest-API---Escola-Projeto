from django.contrib import admin
from .models import Aluno, Disciplina, Nota

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Nota)