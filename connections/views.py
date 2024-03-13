from django.shortcuts import render
from django.http import HttpResponse
from main.models import user, project, offer

def myConnection(request):
    return render(request, "connections_page.html")
