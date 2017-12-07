from django.shortcuts import render
from django.http import HttpResponse
from login.models import claves, registro
from maestro.models import grupo, dias
from login import forms

# Create your views here.

DIAS_SEMANA = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sabado', 'Sabado'),
)

def index(request):
    if 'idUser' in request.session:
        idUser = request.session['idUser']
        nivel = request.session['nivel']
        datos = registro.objects.filter(id=idUser)
        for key in datos:
            usuario = key.usuario

        group = grupo.objects.filter(idMaestro=idUser)
        idDia = []
        for key in group:
            idDia.append(key.id)

        days = dias.objects.filter(idHorario__in=(idDia))

        horario = zip(list(group), list(days))

        return render(request, "home.html", {"usuario": usuario, "nivel":nivel, "horario":horario, "dias":days})

    elif 'iniciar' in request.POST and request.method == "POST":
        usuario = request.POST["usuario"]
        password = request.POST["password"]
        user = registro.objects.filter(usuario = usuario, password = password)
        if user:
            for key in user:
                id = key.id
                nivel = key.nivel
            request.session['idUser'] = str(id)
            request.session['nivel'] = str(nivel)
            nivel = request.session['nivel']
            datos = registro.objects.filter(id=request.session['idUser'])
            for key in datos:
                usuario = key.usuario

            return render(request, "home.html", {"usuario": usuario, "nivel":nivel})
        else:
            return render(request,"index.html", {"form_registro": forms.registro, "form_login": forms.login})

    elif 'registro' in request.POST and request.method == "POST":
        claveUser = request.POST["passwordAccess"]
        if claves.objects.filter(clave=claveUser):
            clave = claves.objects.filter(clave=claveUser)
            for key in clave:
                nivel = key.nivel

            user = registro(
                nombre=request.POST["nombre"],
                usuario=request.POST["usuario"],
                password=request.POST["password"],
                email=request.POST["email"],
                nivel=nivel
            )
            claves.objects.filter(clave=claveUser).delete()
            user.save()
            return render(request,"index.html", {"form_registro": forms.registro, "form_login": forms.login})
        else:
            return HttpResponse("incorrecto")

    else:
        return render(request, 'index.html', {"form_registro": forms.registro, "form_login": forms.login})


def close(request):
    del request.session['idUser']
    del request.session['nivel']

    return render(request, 'index.html', {"form_registro": forms.registro, "form_login": forms.login})