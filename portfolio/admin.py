from django.contrib import admin
from .models import Project
# Register your models here.
#decirle al panel de administrador que aniado estas ventanas

admin.site.register(Project)