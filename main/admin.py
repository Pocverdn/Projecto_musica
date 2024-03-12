from django.contrib import admin
from .models import user, project

# Register your models here.

admin.site.register(user)
admin.site.register(project)