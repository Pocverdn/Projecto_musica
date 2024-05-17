import folium
from django.shortcuts import render, redirect
from django.db.models import Count
import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required

from .models import project, user

band = ""

genre = ""

# Create your views here.

@login_required
def index(request):
    username = request.session.get('logged_in_user', None)
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
    limit_bands = False
    username = request.session.get('logged_in_user', None)
    User = user.objects.get(user_name = username)

    if User.bands is not None:
        bands = [band for band in User.bands.split(',')]

    else:
        bands = [""]

    groups = project.objects.filter(project_name__in=bands)

    print(len(bands))

    if len(bands) >= 3:
        limit_bands = True

    if request.method == 'POST' and 'Borrar' in request.POST:
        band_name = request.POST.get('band_name')
        band = project.objects.get(project_name = band_name)

        band.delete()

        User.delete_band(band_name)

        
        limit_bands = False
        

    return render(request, "groups_page.html", {'groups': groups, 'limit': limit_bands})

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

        username = request.session.get('logged_in_user', None)
        User = user.objects.get(user_name = username)

        User.add_bands(name)
        
        return redirect('groups_page')  
    return render(request, "create_groups.html")

def do_graph():
    data = project.objects.values('location', 'genre').annotate(num_projects=Count('id'))

    # Crear un diccionario para almacenar los datos
    data_dict = {}
    for entry in data:
        location = entry['location']
        genre = entry['genre']
        num_projects = entry['num_projects']
        if location not in data_dict:
            data_dict[location] = {}
        if genre not in data_dict[location]:
            data_dict[location][genre] = num_projects
        else:
            data_dict[location][genre] += num_projects

    # Obtener las ciudades y géneros únicos
    locations = list(data_dict.keys())
    genres = set()
    for projects in data_dict.values():
        genres.update(projects.keys())

    # Crear una barra para cada género en cada ciudad
    width = 0.2
    x = range(len(genres))
    for i, (location, projects) in enumerate(data_dict.items()):
        projects_count = [projects.get(genre, 0) for genre in genres]
        plt.bar([pos + i * width for pos in x], projects_count, width=width, label=location)

    plt.xlabel('Género')
    plt.ylabel('Número de Proyectos')
    plt.title('Proyectos por Género y Ciudad')
    plt.xticks([pos + width * (len(locations) - 1) / 2 for pos in x], list(genres))
    plt.legend(title='Ciudad')

    plt.savefig('media/others/graph.png')


def graph_view(request):
    return render(request, "graph.html")

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

            if r == "Cali":
                popup_content += f"<br>{v[0]}: {v[1]}"
                folium.CircleMarker(location=[3.4516, -76.5320], radius=v[1]*10, color='yellow', fill=True, fill_opacity=v[1]/10, popup=popup_content).add_to(p)
    
    map_html = m._repr_html_()
    map_html2 = p._repr_html_()

    
    if genre['Genre'] == "populares":
        return render(request, 'map.html', {'map_html': map_html2})
    elif genre['Genre'] == "Grafica":
        do_graph()
        return redirect('graph_page')  
    else:
        return render(request, 'map.html', {'map_html': map_html})
