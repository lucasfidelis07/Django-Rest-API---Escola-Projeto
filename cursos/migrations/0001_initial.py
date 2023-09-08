# Generated by Django 4.2.5 on 2023-09-08 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('alunos', models.ManyToManyField(related_name='turmas', to='alunos.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
            ],
        ),
    ]