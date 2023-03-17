from django.shortcuts import render, redirect
from .models import Coordenadas, Meses

# Create your views here.

def heatMap(request):
    coordenadas = Coordenadas.objects.all()
    meses = Meses.objects.all()

    return render(request, "heatMap.html", {"coordenadas": coordenadas, "meses": meses})

# def update(request, id):
#     vmes = request.POST.get("mes")
#     mes = Meses.objects.get(id=id)
#     mes = vmes
#     mes.save()
#     return redirect(home)