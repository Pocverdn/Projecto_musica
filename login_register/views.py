from django.shortcuts import render, redirect
from .forms import RegistroForm
from main.models import user

from django.contrib.auth import authenticate, login

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        prueba = request.POST
        print(prueba)
        username = prueba["username"]
        password = prueba["password1"]
        name = prueba["nombre"]
        surname = prueba["apellido"]
        instruments = prueba["instrumentos"]
        location = prueba["ubicación"]
        genre = prueba["género_biológico"]
        gender = prueba["género_musical"]
        exp = prueba["experiencia_años"]
        description = prueba["descripción"]
        photo = request.FILES.get('photo') if 'photo' in request.FILES else None
        new_user = user( user_name=username, name=name, surname=surname, gender=gender, password=password, instruments=instruments, genre=genre, years=exp, photo=photo, description=description, location=location)
        
        if form.is_valid():
            new_user.save()
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


def custom_login(request):
    global username
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['logged_in_user'] = username
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Credenciales inválidas'})
    
    return render(request, 'registration/login.html')
