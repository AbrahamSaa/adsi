from django.contrib import admin
from login import models

# Register your models here.
class clavesAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nivel')

admin.site.register(models.claves, clavesAdmin)
admin.site.register(models.registro)
