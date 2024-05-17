from django.shortcuts import render, redirect

from main.models import user, project

from .models import offer

# Create your views here.

post_o = ""
band = ""
users = ""
offe = ""

def offers(request):
    return render(request, "offers_page.html")


def choose_band(request):
    username = request.session.get('logged_in_user', None)
    User = user.objects.get(user_name = username)

    bands = [band for band in User.bands.split(',')]
    groups = project.objects.filter(project_name__in=bands)

    contex = {"fil": groups}

    if request.method == 'GET':
        return render(request, "bands_page.html", contex)
    
    else:
        global band
        band = ""
        band=request.POST
        return redirect("/offer_post/")
    
def band_delete (request):
    username = request.session.get('logged_in_user', None)
    User = user.objects.get(user_name = username)

    if User.bands is not None:
        bands = [band for band in User.bands.split(',')]

    else:
        bands = [""]
    groups = project.objects.filter(project_name__in=bands)

    contex = {"fil": groups}

    if request.method == 'GET':
        return render(request, "bands_delete.html", contex)
    
    else:
        global band
        band = ""
        band=request.POST
        return redirect("/offer_delete/")
       

def choose_user(request):
    fil = user.objects.all()
    contex = {"fil": fil}

    if request.method == 'GET':
        return render(request, "user_page.html", contex)
    
    else:
        global users
        users = ""
        users=request.POST
        return redirect("/offer_apply/")


def apply_offer(request):
    fil = offer.objects.all()
    contex = {"fil": fil}
    username = request.session.get('logged_in_user', None)
    User = user.objects.get(user_name = username)

    if request.method == 'GET':
        return render(request, "offers_apply.html", contex)
    
    elif 'project_name' in request.POST:
        global offe
        offe = ""
        offe = request.POST
        ofer = offer.objects.get(tittle_offer=offe['project_name'])
        ofer.add_applicant(User.user_name)
        return redirect("/home/offer/")
        
    elif 'project_delete' in request.POST:
        global offet 
        offet = ""
        offet = request.POST
        ofer = offer.objects.get(tittle_offer=offet['project_delete'])    
        ofer.delete()
        return redirect("/home/offer/")
        
def delete_offer(request):
    fil = offer.objects.filter(group_name=band["project_name"])
    contex = {"fil": fil}

    if request.method == 'GET':
        return render(request, "offers_delete.html", contex)
        
    elif 'project_delete' in request.POST:
        global offet 
        offet = ""
        offet = request.POST
        ofer = offer.objects.get(tittle_offer=offet['project_delete'])    
        ofer.delete()
        return redirect("/home/offer/")        

def offers_post(request):
    if request.method == 'GET':
        return render(request, "offer_post.html")
    
    else:
        global post_o
        post_o = ""
        post_o=request.POST
        
        print(band['project_name'])

        instace = offer()

        instace.tittle_offer = post_o['tittle_offer']
        instace.description_offer = post_o['description_offers']
        instace.group_name = band['project_name']
        instace.gender = post_o['genero de musica']
        instace.instruments = post_o['Instrumentos']
        instace.genre = post_o['Genero']
        instace.years = post_o['Cantidad de eventos']
        instace.location = post_o['Ubicación']

        instace.save()

        print(post_o)
        return redirect("/home/offer/")
    

    
    
    