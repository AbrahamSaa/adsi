from django.db import models

DIAS_SEMANA = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sabado', 'Sabado'),
)

# Create your models here.
class grupo(models.Model):
    idMaestro = models.IntegerField()
    materia = models.CharField(max_length=35)
    aula = models.CharField(max_length=10)
    cupo = models.SmallIntegerField()
    carrera = models.CharField(max_length=25)
    horaInicio = models.CharField(max_length=10)
    horaFinal = models.CharField(max_length=10)

class dias(models.Model):
    idHorario = models.IntegerField()
    lunes = models.CharField(max_length=15)
    martes = models.CharField(max_length=15)
    miercoles = models.CharField(max_length=15)
    jueves = models.CharField(max_length=15)
    viernes = models.CharField(max_length=15)
    sabado = models.CharField(max_length=15)

class date(models.Model):
    date = models.CharField(max_length=10)
    idgroup = models.IntegerField(null=True)

class groupAsistencia(models.Model):
    idA = models.IntegerField()
    idD = models.IntegerField()
    status = models.CharField(max_length=1)

class alumnos(models.Model):
    expediente = models.SmallIntegerField()
    nombre = models.CharField(max_length=60)
    carrera = models.CharField(max_length=30)

class clases(models.Model):
    idAlumno = models.SmallIntegerField()
    idClase = models.SmallIntegerField()

class calificacion(models.Model):
    idCalif = models.IntegerField()
    idAlumno = models.IntegerField()
    calif = models.IntegerField()

class calificacionAlumno(models.Model):
    parcial = models.IntegerField()
    idGrupo = models.IntegerField()

class calificacionProject(models.Model):
    idCalif = models.IntegerField()
    idAlumno = models.IntegerField()
    calif = models.IntegerField()

class calificacionAlumnoProject(models.Model):
    project = models.IntegerField()
    idGrupo = models.IntegerField()

class metricasGroup(models.Model):
    idGrupo = models.SmallIntegerField()
    num_exam = models.SmallIntegerField()
    num_proy = models.SmallIntegerField()
    num_retardos = models.SmallIntegerField()
    exam_avg = models.FloatField()
    proyect_avg = models.FloatField()
    atten_avg = models.FloatField()
    part_avg = models.FloatField()
    tareas_avg = models.FloatField()

class worksCalif(models.Model):
    idWork = models.IntegerField()
    idAlumno = models.IntegerField()
    calif = models.CharField(max_length=2)

class works(models.Model):
    type = models.CharField(max_length=2)
    date = models.CharField(max_length=10)
    idGrupo = models.IntegerField()