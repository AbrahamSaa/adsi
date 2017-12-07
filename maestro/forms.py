from django import forms

class grupo(forms.Form):
    materia = forms.CharField(max_length=35)
    aula = forms.CharField(max_length=10)
    cupo = forms.IntegerField()
    carrera = forms.CharField(max_length=25)
    horaInicio = forms.CharField(label="Inicio de clase", max_length=10,widget=forms.TextInput(attrs={'class':'timepicker'}))
    horaFinal = forms.CharField(label="Termino de clase",max_length=10,widget=forms.TextInput(attrs={'class':'timepicker'}))

