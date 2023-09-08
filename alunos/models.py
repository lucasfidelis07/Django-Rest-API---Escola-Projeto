from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno, related_name='disciplinas')

    def __str__(self):
        return self.nome

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} - {}" .format(self.aluno, self.disciplina)