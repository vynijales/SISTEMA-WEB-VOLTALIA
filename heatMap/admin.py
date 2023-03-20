from django.contrib import admin
from .models import Coordenadas, Meses, Data


# Register your models here.
admin.site.register(Coordenadas)
admin.site.register(Meses)
admin.site.register(Data)