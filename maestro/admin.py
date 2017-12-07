from django.contrib import admin
from maestro import models

# Register your models here.

admin.site.register(models.grupo)
admin.site.register(models.dias)
admin.site.register(models.groupAsistencia)
admin.site.register(models.alumnos)
admin.site.register(models.clases)
admin.site.register(models.date)
admin.site.register(models.calificacion)
admin.site.register(models.calificacionAlumno)
admin.site.register(models.metricasGroup)
admin.site.register(models.worksCalif)
admin.site.register(models.works)
admin.site.register(models.calificacionProject)
admin.site.register(models.calificacionAlumnoProject)


