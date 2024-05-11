"""
URL configuration for BandMate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from filter import views as filterViews
from main import views as mainViews
from offer import views as offerViews
from connections import views as connectionsViews
from django.conf.urls.static import static
from django.conf import settings
from login_register import views as viewsRegister

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', auth_views.LoginView.as_view(), name='login'),  
    path('home/', mainViews.index, name='home'), 
    path('map_page/', mainViews.map_view),
    path('graph_page/', mainViews.graph_view,  name='graph_page'),
    path('map_connect/', mainViews.map_connect),
    path('home/offer/', offerViews.offers),
    path('offer_post/', offerViews.offers_post),
    path('band_page/', offerViews.choose_band),
    path('band_delete/', offerViews.band_delete),
    path('user_page/', offerViews.choose_user),
    path('offer_apply/', offerViews.apply_offer),
    path('offer_delete/', offerViews.delete_offer),
    path('user_filter/', filterViews.filter_user),
    path('project_filter/', filterViews.filter_project),
    path('result_user/', filterViews.result_user),
    path('result_project/', filterViews.result_project),
    path('connections/', connectionsViews.myConnection),
    path('band_page_conections/', connectionsViews.choose_band),
    path('offers_page_connections/', connectionsViews.chosse_offer),
    path('home/groups_page/', mainViews.groups,  name='groups_page'),
    path('create_group/', mainViews.create_groups, name = 'create_groups'),
    path('registro/', viewsRegister.registro, name='registro'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
