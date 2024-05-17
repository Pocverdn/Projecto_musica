from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import user, project
from offer.models import offer

band = ""
offe = ""


def choose_band(request):
    username = request.session.get('logged_in_user', None)
    User = user.objects.get(user_name = username)

    bands = [band for band in User.bands.split(',')]
    groups = project.objects.filter(project_name__in=bands)

    contex = {"fil": groups}

    

    if request.method == 'GET':
        return render(request, "bands_page_connections.html", contex)
    
    else:
        global band
        band = ""
        band=request.POST
        print(band)
        return redirect("/offers_page_connections/")
    

def chosse_offer(request):
    global band
    fil = offer.objects.filter(group_name=band["project_name"])
    contex = {"fil": fil}

    if request.method == 'GET':
        return render(request, "offers_connections.html", contex)
    
    else:
        global offe
        offe = ""
        offe=request.POST
        print(offe)
        return redirect("/connections/")


def myConnection(request):
    global offe
    fil = offer.objects.filter(tittle_offer=offe["tittle_offer"])
    names = [name for name in fil[0].applicants.split(',')]
    print(names)
    fil2 = user.objects.all()
    contex = {"fil2": fil2, 'names': names, 'offe': fil}
    return render(request, "connections_page.html", contex)