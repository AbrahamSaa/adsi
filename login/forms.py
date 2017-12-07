from django import forms

class registro(forms.Form):
    nombre = forms.CharField(max_length=60)
    usuario = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    email = forms.EmailField(max_length=50)
    passwordAccess = forms.IntegerField(label="Codigo de acceso")

class login(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}))
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'validate'}))
