import folium
from django.shortcuts import render, redirect
from django.db.models import Count

from .models import project

band = ""

genre = ""

# Create your views here.

def index(request):
    return render(request, "index.html")


def map_connect(request):

    if request.method == 'GET':
        return render(request, "connection_map.html",)
    
    else:
        global genre
        genre = ""
        genre=request.POST
        print(genre['Genre'])
        return redirect("/map_page/")
    


def groups(request):
    groups = project.objects.all()
    return render(request, "groups_page.html", {'groups': groups})

def create_groups(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        location = request.POST.get('location')
        integrants = request.POST.get('integrantes')
        exp = request.POST.get('exp')
        img = request.FILES.get('img')
        
        print(integrants)
        print(exp)

        group = project(project_name=name, genre=genre, location=location, photo_project=img, description=description, num_events=exp, num_integrants=integrants)
        group.save()
        
        return redirect('groups_page')  
    return render(request, "create_groups.html")



def map_view(request):

    bands = project.objects.all()

    cities = project.objects.values_list('location', flat=True).distinct()

    results = {}

    for city in cities:
        genero = project.objects.filter(location=city).values('genre').annotate(num_proyectos=Count('genre')).order_by('-num_proyectos').first()
        
        city_result = []

        city_result.append(genero['genre'])
        city_result.append(genero['num_proyectos'])
        
        results[city] = city_result


    print(results)

    global genre

    M = 0
    B = 0
    C = 0

    for band in bands:
        if band.location == "Medellin" and genre['Genre'] == band.genre:
            M = M+1

        if band.location == "Bogota" and genre['Genre'] == band.genre:
            B= B+1

        if band.location == "Cali" and genre['Genre'] == band.genre:
            C = C+1


    print(M)

    m = folium.Map(location=[5.5243, -75.0636], zoom_start=8)
    p = folium.Map(location=[5.5243, -75.0636], zoom_start=8)

    cities = [
        {"name": "Medellin", "coordinates": [6.2442, -75.5812], "M": M},
        {"name": "Bogota", "coordinates": [4.6243, -74.0636], "B": B},
        {"name": "Cali", "coordinates": [3.4516, -76.5320], "C": C}
    ]


    for city in cities:
        popup_content = f"<b>{city['name']}</b>"
        if city["name"] == "Medellin" and M>0:
            popup_content += f"<br>{genre['Genre']}: {city['M']}"
            folium.CircleMarker(location=city["coordinates"], radius=M*10, color='blue', fill=True, fill_opacity=M/10, popup=popup_content).add_to(m)

        if city["name"] == "Bogota" and B>0:
            popup_content += f"<br>{genre['Genre']}: {city['B']}"
            folium.CircleMarker(location=city["coordinates"], radius=B*10, color='red', fill=True, fill_opacity=B/10, popup=popup_content).add_to(m)

        if city["name"] == "Cali" and C>0:
            popup_content += f"<br>{genre['Genre']}: {city['C']}"
            folium.CircleMarker(location=city["coordinates"], radius=C*10, color='yellow', fill=True, fill_opacity=C/10, popup=popup_content).add_to(m)


        for r, v in results.items():
            popup_content = f"<b>{r}</b>"
            if r == "Medellin":
                popup_content += f"<br>{v[0]}: {v[1]}"
                folium.CircleMarker(location=[6.2442, -75.5812], radius=v[1]*10, color='blue', fill=True, fill_opacity=v[1]/10, popup=popup_content).add_to(p)

            if r == "Bogota":
                popup_content += f"<br>{v[0]}: {v[1]}"
                folium.CircleMarker(location=[4.6243, -74.0636], radius=v[1]*10, color='red', fill=True, fill_opacity=v[1]/10, popup=popup_content).add_to(p)

            if r == "Cali" and C>0:
                popup_content += f"<br>{v[0]}: {v[1]}"
                folium.CircleMarker(location=[3.4516, -76.5320], radius=v[1]*10, color='yellow', fill=True, fill_opacity=v[1]/10, popup=popup_content).add_to(p)
    
    map_html = m._repr_html_()
    map_html2 = p._repr_html_()

    
    if genre['Genre'] == "populares":
        return render(request, 'map.html', {'map_html': map_html2})
    else:
        return render(request, 'map.html', {'map_html': map_html})
