from django.db import models

# Create your models here.

class estudiante(models.Model):
    cedula= models.CharField(max_length=20, primary_key=True)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=50)

class materia(models.Model):
    nombre= models.CharField(max_length=50)
    estudiantes= models.ManyToManyField(estudiante)

class horario(models.Model):
    horas_dis= models.CharField(max_length=50)
    horarios= models.ManyToManyField(estudiante)