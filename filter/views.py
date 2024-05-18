from django.shortcuts import render, redirect

# Create your views here.

from main.models import user, project

from django.urls import reverse

import globals

results_user = ""
results_project = ""

def filter_user(request):
    fil = user.objects.all()
    contex = {"fil": fil}
    searchTerm = request.GET.get('searchMusician')

    if searchTerm:
        musicians=user.objects.filter(user_name__icontains=searchTerm)

        if request.method == 'POST':
            data = ""
            data=request.POST
            print(data)

            globals.user_name = data['band_name']


            print(globals.user_name)

            return redirect(reverse('profile'))
        
                
        contexBN = {"searchTerm": searchTerm, "musicians": musicians}
        return render(request, "results_byname_user.html", contexBN)


    if request.method == 'GET':
        return render(request, "user_filter.html", contex)

    else:
        global results_user
        results_user=request.POST
        return redirect("/result_user/")
    
def filter_project(request):
    fil = project.objects.all()
    contex = {"fil": fil}

    searchTerm = request.GET.get('searchProjects')

    if searchTerm:

        if request.method == 'POST':
            data = ""
            data=request.POST
            print(data)

            globals.project_name = data['band_name']


            print(globals.project_name)

            return redirect(reverse('group_profile'))
        
        projects=project.objects.filter(project_name__icontains=searchTerm)
        contexBN = {"searchTerm": searchTerm, "projects": projects}
        return render(request, "results_byname_project.html", contexBN)


    if request.method == 'GET':
        return render(request, "project_filter.html", contex)

    else:
        global results_project
        results_project=request.POST
        return redirect("/result_project/")
    

def result_user(request):

    if request.method == 'POST':
        data = ""
        data=request.POST
        print(data)

        globals.user_name = data['band_name']


        print(globals.user_name)

        return redirect(reverse('profile'))

    fil = user.objects.all()
    values = list(results_user.values())[1:] 
    if values[1] != "space":
        v_1 = int(values[1])
        values[1] = v_1

    return render(request, "results_filter_user.html", {'values': values, 'fil': fil})


def result_project(request):

    if request.method == 'POST':
        data = ""
        data=request.POST
        print(data)

        globals.project_name = data['band_name']


        print(globals.project_name)

        return redirect(reverse('group_profile'))

    fil = project.objects.all()
    values = list(results_project.values())[1:] 
    print(values)
    if values[0] != "space":
        v_0 = int(values[0])
        values[0] = v_0

    if values[2] != "space":
        v_2 = int(values[2])
        values[2] = v_2
    
    return render(request, "results_filter_project.html", {'values': values, 'fil': fil})