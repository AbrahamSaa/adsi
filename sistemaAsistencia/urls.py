"""sistemaAsistencia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from login import views
import maestro.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="login"),
    url(r'^close$', views.close, name="close"),
    url(r'^addGroup/$', maestro.views.crearGrupo, name="agregarGrupos"),
    url(r'^setGroup/$', maestro.views.setGrupo, name="setGrupos"),
    url(r'^deletesGroup/(?P<id_group>\d+)/', maestro.views.deletesGroup, name="deletesGroup"),
    url(r'^addAlumnos/(?P<id_group>\d+)/', maestro.views.addAlumnos, name="addAlumnos"),
    url(r'^addAlumnosurl/', maestro.views.addAlumnosurl, name="addAlumnosurl"),
    url(r'^getAlumnos/', maestro.views.getAlumnos, name="getAlumnos"),
    url(r'^deleteStudent/', maestro.views.deleteStudent, name="delStudent"),
    url(r'^asistencia/', maestro.views.asistencia, name="asistencia"),
    url(r'^asistenciagrupo/(?P<id_group>\d+)/', maestro.views.asistenciaGrupo, name="asistenciaGrupo"),
    url(r'^selectAsistencia/$', maestro.views.selectAsistencia, name="selectAsistencia"),
    url(r'^updateAt/$', maestro.views.updateAt, name="updateAt"),
    url(r'^exam/$', maestro.views.examen, name="exam"),
    url(r'^exam/(?P<id_group>\d+)/$', maestro.views.examenGroup, name="examenGroup"),
    url(r'^setExamCalif/$', maestro.views.setExamCalif, name="setExamCalif"),
    url(r'^setCalifStudent/$', maestro.views.setCalifStudent, name="setCalifStudent"),
    url(r'^addMetricas/$', maestro.views.addMetricas, name="addMetricas"),
    url(r'^project/$', maestro.views.proyecto, name="proyecto"),
    url(r'^project/(?P<id_group>\d+)/$', maestro.views.proyectoG, name="proyectoG"),
    url(r'^setProjectCalif/$', maestro.views.setProjectCalif, name="setProjectCalif"),
    url(r'^setCalifStudentProject/$', maestro.views.setCalifStudentProject, name="setCalifStudentProject"),
    url(r'^works/$', maestro.views.worksV, name="works"),
    url(r'^works/(?P<id_group>\d+)/$', maestro.views.worksG, name="worksG"),
    url(r'^worksList/$', maestro.views.worksList, name="worksList"),
    url(r'^worksSet/$', maestro.views.worksSet, name="worksSet"),
    url(r'^report/$', maestro.views.report, name="report"),
    url(r'^report/(?P<id_group>\d+)/$', maestro.views.reportN, name="reportN"),
    url(r'^getCalifStudent/$', maestro.views.getCalifStudent, name="getCalifStudent"),
]
