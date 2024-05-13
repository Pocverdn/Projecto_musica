from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

opciones_numeros = [(str(i), str(i)) for i in range(6)]
class RegistroForm(UserCreationForm):
    instrumentos = forms.ChoiceField(choices=(('G', 'Guitarra'), ('Pn', 'Piano'), ('Bat', 'Batería'), ('Baj', 'Bajo')))
    ubicación = forms.ChoiceField(choices=(('C', 'Cali'), ('Mde', 'Medellín'), ('Bgta', 'Bogotá')))
    género_biológico = forms.ChoiceField(choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
    género_musical = forms.ChoiceField(choices=(('R', 'Rock'), ('P', 'Pop'), ('J', 'Jazz'), ('S', 'Salsa'), ('M', 'Metal')))
    experiencia_años= forms.ChoiceField(choices=opciones_numeros)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    descripción = forms.CharField(max_length=500, widget=forms.Textarea)
    foto = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].error_messages = {'required': ''}
            self.fields[field_name].help_text = None 

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido','instrumentos', 'ubicación', 'género_biológico', 'género_musical', 'experiencia_años', 'descripción', 'foto']

