from django.shortcuts import render
from maestro import forms
from maestro.models import grupo, dias, alumnos, clases, date, groupAsistencia, \
    calificacion, calificacionAlumno, metricasGroup, calificacionAlumnoProject,\
    calificacionProject, works, worksCalif
from login.models import registro
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

# Create your views here.

horaDia = ""
DIAS_SEMANA = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sabado', 'Sabado'),
)

messageDelete = False

def crearGrupo(request):
    if 'idUser' in request.session:
        if request.method == "POST":
            daysGet = request.POST.getlist('days[]')

            idUser = request.session['idUser']
            horario = grupo(
                idMaestro=idUser,
                materia=request.POST["materia"],
                aula=request.POST["aula"],
                cupo=request.POST["cupo"],
                carrera=request.POST["carrera"],
                horaInicio=request.POST["horaInicio"],
                horaFinal = request.POST["horaFinal"],
            )
            horaDia = request.POST["horaInicio"] + " - " + request.POST["horaFinal"]
            horario.save()

            days = dias(
                idHorario=horario.id,
                lunes=gethorario("Lunes",daysGet, horaDia),
                martes=gethorario("Martes",daysGet, horaDia),
                miercoles=gethorario("Miercoles",daysGet, horaDia),
                jueves=gethorario("Jueves",daysGet, horaDia),
                viernes=gethorario("Viernes",daysGet, horaDia),
                sabado=gethorario("Sabado",daysGet, horaDia),
            )
            message = True
            days.save()
            idUser = request.session['idUser']
            nivel = request.session['nivel']
            datos = registro.objects.filter(id=idUser)

            for key in datos:
                nombre = key.nombre
                usuario = key.usuario


            return render(request, 'addGroups.html', {
                "form_grupo": forms.grupo,
                "usuario": usuario,
                "nivel": nivel,
                "dias": DIAS_SEMANA,
                "ingreso": message,
            })

        message = False
        idUser = request.session['idUser']
        nivel = request.session['nivel']
        datos = registro.objects.filter(id=idUser)

        for key in datos:
            usuario = key.usuario

        return render(request, 'addGroups.html', {
            "form_grupo":forms.grupo,
            "usuario": usuario,
            "nivel": nivel,
            "dias":DIAS_SEMANA,
            "ingreso":message,
        })

def setGrupo(request):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    datos = registro.objects.filter(id=idUser)

    group = grupo.objects.filter(idMaestro=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'setGroups.html',{
        "usuario":usuario,
        "nivel": nivel,
        "horario":group,
        "messageDelete":False,
    })

def deletesGroup(request, id_group):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    group = grupo.objects.filter(idMaestro=idUser)
    datos = registro.objects.filter(id=idUser)

    for key in datos:
        usuario = key.usuario

    for key in group:
        if int(id_group) == int(key.id):
            grupo.objects.get(id=id_group).delete()
            return render(request, 'setGroups.html', {
                "usuario": usuario,
                "nivel": nivel,
                "horario": group,
                "messageDelete": True,
            })



def addAlumnos(request, id_group):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    group = grupo.objects.filter(id=id_group)
    datos = registro.objects.filter(id=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'addAlumnos.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
        "messageDelete": False,
    })

def gethorario(dia,daysGet, horaDia):
    if dia in daysGet:
        return horaDia
    else:
        return "-"

def proyecto(request):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    datos = registro.objects.filter(id=idUser)

    group = grupo.objects.filter(idMaestro=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'proyecto.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
        "messageDelete": False,
    })

def worksV(request):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    datos = registro.objects.filter(id=idUser)

    group = grupo.objects.filter(idMaestro=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'works.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
        "messageDelete": False,
    })

def report(request):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    datos = registro.objects.filter(id=idUser)

    group = grupo.objects.filter(idMaestro=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'report.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
        "messageDelete": False,
    })

def proyectoG(request,id_group):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    group = grupo.objects.filter(pk=id_group)
    metrica = metricasGroup.objects.filter(idGrupo=id_group)
    datos = registro.objects.filter(id=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'proyectoGroup.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
        "metrica":metrica,
    })

def worksG(request, id_group):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    group = grupo.objects.filter(pk=id_group)
    metrica = metricasGroup.objects.filter(idGrupo=id_group)
    datos = registro.objects.filter(id=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'worksGroup.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
        "metrica": metrica,
    })

def reportN(request, id_group):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    group = grupo.objects.filter(pk=id_group)
    metrica = metricasGroup.objects.filter(idGrupo=id_group)
    datos = registro.objects.filter(id=idUser)

    clase = clases.objects.filter(idClase=id_group)

    idAlumnos = []
    for key in clase:
        idAlumnos.append(key.idAlumno)

    countAttendence = date.objects.filter(idgroup=id_group).count()
    countWorksHomeWork = works.objects.filter(idGrupo=id_group,type="T").count()
    countWorksProject = works.objects.filter(idGrupo=id_group,type="P").count()

    alumnosLista = alumnos.objects.filter(id__in=(idAlumnos))

    for key in datos:
        usuario = key.usuario

    return render(request, 'reportFull.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
        "metrica": metrica,
        "alumnosLista":alumnosLista,
        "totalAttendece":countAttendence,
        "totalHomeworks":countWorksHomeWork,
        "totalProjects":countWorksProject,
    })

@csrf_exempt
def addAlumnosurl(request):
    if request.is_ajax():
        if request.POST['nombre'] and request.POST["exp"] and request.POST["carrera"]:
            alumno = alumnos(
                nombre=request.POST["nombre"],
                expediente=request.POST["exp"],
                carrera=request.POST["carrera"]
            )
            alumno.save()
            clase = clases(
                idAlumno=alumno.id,
                idClase=request.POST["id"]
            )
            clase.save()
            clase.clean()
            alumno.clean()
            return HttpResponse(True)

@csrf_exempt
def getAlumnos(request):
    if request.is_ajax():
        clase = clases.objects.filter(idClase=request.POST["id"])

        idAlumnos = []
        for key in clase:
            idAlumnos.append(key.idAlumno)

        alumnosLista = alumnos.objects.filter(id__in=(idAlumnos))


        data = serializers.serialize("json", alumnosLista)
        return HttpResponse(data)

@csrf_exempt
def deleteStudent(request):
    if request.is_ajax():
        alumnos.objects.filter(id=request.POST["id"]).delete()
        clases.objects.filter(idAlumno=request.POST["id"]).delete()
        groupAsistencia.objects.filter(idA=request.POST["id"]).delete()
        calificacionProject.objects.filter(idAlumno=request.POST["id"]).delete()
        calificacion.objects.filter(idAlumno=request.POST["id"]).delete()
        worksCalif.objects.filter(idAlumno=request.POST["id"]).delete()
        return HttpResponse(True)

def asistencia(request):
    idUser = request.session['idUser']
    datos = registro.objects.filter(id=idUser)

    group = grupo.objects.filter(idMaestro=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'asistencia.html', {
        "usuario":usuario,
        "horario": group,
        })

def asistenciaGrupo(request,id_group):
    idUser = request.session['idUser']
    datos = registro.objects.filter(id=idUser)

    group = grupo.objects.filter(pk=id_group)

    for key in datos:
        usuario = key.usuario

    return render(request, 'asistenciaGrupo.html', {
        "usuario": usuario,
        "horario": group,
    })

@csrf_exempt
def selectAsistencia(request):
    if request.is_ajax():
        dateSel = request.POST["dateSel"]
        dateArray = date.objects.filter(date=dateSel, idgroup=request.POST["id"])

        if not dateArray:
            dateUpload = date(date=dateSel,idgroup=request.POST["id"])
            dateUpload.save()
            idDateU = dateUpload.id
            idGrupoActual = request.POST["id"]

            clase = clases.objects.filter(idClase=idGrupoActual)

            for key in clase:
                groupAsistencia(
                    idA=key.idAlumno,
                    idD=idDateU,
                    status=" ",
                ).save()

            alumnoAsistencia = groupAsistencia.objects.filter(idD=idDateU)
            alumnosList = []

            for key in alumnoAsistencia:
                alumnosList.append(key.idA)

            all_objects = list(alumnos.objects.filter(id__in=(alumnosList))) + list(groupAsistencia.objects.filter(idD=idDateU))

            data = serializers.serialize("json", all_objects)
            return HttpResponse(data)

        else:
            dateGet = date.objects.filter(date=dateSel,idgroup=request.POST["id"])

            for key in dateGet:
                id = key.id

            alumnoAsistencia = groupAsistencia.objects.filter(idD=id)

            alumnosList = []
            for key in alumnoAsistencia:
                alumnosList.append(key.idA)

            all_objects = list(alumnos.objects.filter(id__in=(alumnosList))) + list(groupAsistencia.objects.filter(idD=id))

            data = serializers.serialize("json", all_objects)
            return HttpResponse(data)

@csrf_exempt
def updateAt(request):
    if request.is_ajax():
        dateUpdate = date.objects.filter(date=request.POST["dateSel"],idgroup=request.POST["id"])

        for key in dateUpdate:
            asistenciaAlumno = groupAsistencia.objects.get(idD=key.id, idA = request.POST["idAlumno"])

        asistenciaAlumno.status = request.POST["status"]
        asistenciaAlumno.save()

        return HttpResponse(True)

def examen(request):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    group = grupo.objects.filter(idMaestro=idUser)
    datos = registro.objects.filter(id=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'examen.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
    })

def examenGroup(request,id_group):
    idUser = request.session['idUser']
    nivel = request.session['nivel']
    group = grupo.objects.filter(pk=id_group)
    metrica = metricasGroup.objects.filter(idGrupo=id_group)
    datos = registro.objects.filter(id=idUser)

    for key in datos:
        usuario = key.usuario

    return render(request, 'examenGroup.html', {
        "usuario": usuario,
        "nivel": nivel,
        "horario": group,
        "metrica":metrica
    })

@csrf_exempt
def setExamCalif(request):
    if request.is_ajax():
        dataC = calificacionAlumno.objects.filter(idGrupo=request.POST["id"],parcial=request.POST["parcial"])

        if not dataC:
            dataUpload = calificacionAlumno(idGrupo=request.POST["id"], parcial=request.POST["parcial"])
            dataUpload.save()
            idDataU = dataUpload.id
            idGrupoActual = request.POST["id"]

            clase = clases.objects.filter(idClase=idGrupoActual)

            for key in clase:
                calificacion(
                    idAlumno=key.idAlumno,
                    idCalif=idDataU,
                    calif=0,
                ).save()

            alumnoCalif = calificacion.objects.filter(idCalif=idDataU)
            alumnosList = []

            for key in alumnoCalif:
                alumnosList.append(key.idAlumno)

            all_objects = list(alumnos.objects.filter(id__in=(alumnosList))) + list(
                 calificacion.objects.filter(idCalif=idDataU))

            data = serializers.serialize("json", all_objects)
            return HttpResponse(data)

        else:
            dataGet = calificacionAlumno.objects.filter(idGrupo=request.POST["id"], parcial=request.POST["parcial"])

            for key in dataGet:
                id = key.id


            alumnoCalif = calificacion.objects.filter(idCalif=id)

            alumnosList = []
            for key in alumnoCalif:
                alumnosList.append(key.idAlumno)

            all_objects = list(alumnos.objects.filter(id__in=(alumnosList))) + list(
                calificacion.objects.filter(idCalif=id))

            data = serializers.serialize("json", all_objects)
            return HttpResponse(data)

@csrf_exempt
def worksList(request):
    if request.is_ajax():
        dataC = works.objects.filter(idGrupo=request.POST["id"], type=request.POST["type"], date=request.POST["date"])

        if not dataC:
            dataUpload = works(idGrupo=request.POST["id"], type=request.POST["type"], date=request.POST["date"])
            dataUpload.save()
            idDataU = dataUpload.id
            idGrupoActual = request.POST["id"]

            clase = clases.objects.filter(idClase=idGrupoActual)

            for key in clase:
                worksCalif(
                    idAlumno=key.idAlumno,
                    idWork=idDataU,
                    calif=' ',
                ).save()

            alumnoCalif = worksCalif.objects.filter(idWork=idDataU)
            alumnosList = []

            for key in alumnoCalif:
                alumnosList.append(key.idAlumno)

            all_objects = list(alumnos.objects.filter(id__in=(alumnosList))) + list(
                worksCalif.objects.filter(idWork=idDataU))

            data = serializers.serialize("json", all_objects)
            return HttpResponse(data)

        else:
            dataGet = works.objects.filter(idGrupo=request.POST["id"], type=request.POST["type"], date=request.POST["date"])

            for key in dataGet:
                id = key.id

            alumnoCalif = worksCalif.objects.filter(idWork=id)

            alumnosList = []
            for key in alumnoCalif:
                alumnosList.append(key.idAlumno)

            all_objects = list(alumnos.objects.filter(id__in=(alumnosList))) + list(
                worksCalif.objects.filter(idWork=id))

            data = serializers.serialize("json", all_objects)
            return HttpResponse(data)

@csrf_exempt
def setProjectCalif(request):
    if request.is_ajax():
        dataC = calificacionAlumnoProject.objects.filter(idGrupo=request.POST["id"], project=request.POST["metrica"])

        if not dataC:
            dataUpload = calificacionAlumnoProject(idGrupo=request.POST["id"], project=request.POST["metrica"])
            dataUpload.save()
            idDataU = dataUpload.id
            idGrupoActual = request.POST["id"]

            clase = clases.objects.filter(idClase=idGrupoActual)

            for key in clase:
                calificacionProject(
                    idAlumno=key.idAlumno,
                    idCalif=idDataU,
                    calif=0,
                ).save()

            alumnoCalif = calificacionProject.objects.filter(idCalif=idDataU)
            alumnosList = []

            for key in alumnoCalif:
                alumnosList.append(key.idAlumno)

            all_objects = list(alumnos.objects.filter(id__in=(alumnosList))) + list(
                 calificacionProject.objects.filter(idCalif=idDataU))

            data = serializers.serialize("json", all_objects)
            return HttpResponse(data)

        else:
            dataGet = calificacionAlumnoProject.objects.filter(idGrupo=request.POST["id"], project=request.POST["metrica"])

            for key in dataGet:
                id = key.id

            alumnoCalif = calificacionProject.objects.filter(idCalif=id)

            alumnosList = []
            for key in alumnoCalif:
                alumnosList.append(key.idAlumno)

            all_objects = list(alumnos.objects.filter(id__in=(alumnosList))) + list(
                calificacionProject.objects.filter(idCalif=id))

            data = serializers.serialize("json", all_objects)
            return HttpResponse(data)

@csrf_exempt
def setCalifStudentProject(request):
    if request.is_ajax():
        calif = calificacionProject.objects.get(idCalif=request.POST["idCalif"], idAlumno=request.POST["id"])
        calif.calif = request.POST["calif"]
        calif.save()
        return HttpResponse(True)

@csrf_exempt
def setCalifStudent(request):
    if request.is_ajax():
        calif = calificacion.objects.get(idCalif=request.POST["idCalif"], idAlumno=request.POST["id"])
        calif.calif = request.POST["calif"]
        calif.save()
        return HttpResponse(True)

@csrf_exempt
def worksSet(request):
    if request.is_ajax():
        calif = worksCalif.objects.get(idWork=request.POST["idWork"], idAlumno=request.POST["idalumno"])
        calif.calif = request.POST["status"]
        calif.save()
        return HttpResponse(True)

@csrf_exempt
def addMetricas(request):
    if request.is_ajax():
        metricas = metricasGroup.objects.filter(idGrupo=request.POST["id_group"])

        if not metricas:
            metricasGroup(
                idGrupo=request.POST["id_group"],
                num_exam=request.POST["exam_num"],
                num_proy=request.POST["proy_num"],
                num_retardos=request.POST["asis_num"],
                exam_avg=request.POST["exam_por"],
                proyect_avg=request.POST["proy_por"],
                atten_avg=request.POST["asis_por"],
                part_avg=request.POST["part_por"],
                tareas_avg=request.POST["tar_por"],
            ).save()
            return HttpResponse(True)
        else:
            metricasEdit = metricasGroup.objects.get(idGrupo=request.POST["id_group"])
            metricasEdit.idGrupo=request.POST["id_group"]
            metricasEdit.num_exam=request.POST["exam_num"]
            metricasEdit.num_proy=request.POST["proy_num"]
            metricasEdit.num_retardos=request.POST["asis_num"]
            metricasEdit.exam_avg=request.POST["exam_por"]
            metricasEdit.proyect_avg=request.POST["proy_por"]
            metricasEdit.atten_avg=request.POST["asis_por"]
            metricasEdit.part_avg=request.POST["part_por"]
            metricasEdit.tareas_avg=request.POST["tar_por"]


            metricasEdit.save()
            return HttpResponse(True)

@csrf_exempt
def getCalifStudent(request):
    if request.is_ajax():

        getWorkT = works.objects.filter(idGrupo=request.POST["idgroup"],type="T")
        getWorkP = works.objects.filter(idGrupo=request.POST["idgroup"],type="P")
        getDate  = date.objects.filter(idgroup=request.POST["idgroup"])
        getCalifA= calificacionAlumno.objects.filter(idGrupo=request.POST["idgroup"])
        getCalifP= calificacionAlumnoProject.objects.filter(idGrupo=request.POST["idgroup"])

        idP = []
        idT = []
        idD = []
        idC = []
        idPj = []

        for key in getWorkP:
            idP.append(key.id)

        for key in getWorkT:
            idT.append(key.id)

        for key in getDate:
            idD.append(key.id)

        for key in getCalifA:
            idC.append(key.id)

        for key in getCalifP:
            idC.append(key.id)

        countTareas = worksCalif.objects.filter(idWork__in=(idT),calif='E',idAlumno=request.POST["id"]).count()
        countPartic = worksCalif.objects.filter(idWork__in=(idP),calif='P',idAlumno=request.POST["id"]).count()
        countAtten = groupAsistencia.objects.filter(idD__in=(idD),status="A",idA=request.POST["id"]).count()
        countAttenF = groupAsistencia.objects.filter(idD__in=(idD),status="F",idA=request.POST["id"]).count()
        calif = list(calificacion.objects.filter(idCalif__in=(idC),idAlumno=request.POST["id"]).values("calif"))
        califP = list(calificacionProject.objects.filter(idCalif__in=(idC),idAlumno=request.POST["id"]).values("calif"))

        result = {}
        result["Tareas"] = countTareas
        result["Participacion"] = countPartic
        result["Asistencia"] = countAtten
        result["Faltas"] = countAttenF
        result["Examen"] = calif
        result["Proyecto"] = califP

        return HttpResponse(json.dumps(result), content_type='application/json')