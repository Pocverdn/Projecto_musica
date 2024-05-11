from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    instrumentos = forms.CharField(max_length=100)
    ubicación = forms.CharField(max_length=100)
    género_biológico = forms.ChoiceField(choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
    género_musical = forms.CharField(max_length=100)
    experiencia = forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].error_messages = {'required': ''}

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido','instrumentos', 'ubicación', 'género_biológico', 'género_musical', 'experiencia']

