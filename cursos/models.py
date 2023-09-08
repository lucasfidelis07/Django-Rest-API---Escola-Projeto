from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alunos = models.ManyToManyField('alunos.Aluno', related_name='turmas')

    def __str__(self):
        return "{} - {}" .format(self.curso - self.nome)
