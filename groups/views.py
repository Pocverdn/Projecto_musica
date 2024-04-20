from django.shortcuts import render, redirect
from .models import Group

def groups(request):
    groups = Group.objects.all()
    return render(request, "groups_page.html", {'groups': groups})

def create_groups(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        location = request.POST.get('location')
        img = request.FILES.get('img')
        
        group = Group(name=name, description=description, genre=genre, location=location, img=img)
        group.save()
        
        return redirect('groups_page')  
    return render(request, "create_groups.html")
