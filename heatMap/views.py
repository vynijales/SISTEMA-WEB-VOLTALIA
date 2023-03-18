from django.shortcuts import render, redirect
from .models import Coordenadas, Meses
import json

# Create your views here.

def heatMap(request):
    coordenadas = Coordenadas.objects.all()
    meses = Meses.objects.all()
    print(request)
    coordenadas_list = [[float(coord.longitude), float(coord.latitude)] for coord in coordenadas]
    
    lista = []
    for coord, mes in zip(coordenadas, meses):
        lista.append([float(coord.latitude), float(coord.longitude)])

    context = {
        "coordenadas": coordenadas,
        "meses": meses,
        # "coordenadas_json": json.dumps(coordenadas_list),
        "teste": lista,
        "coordenadas_list": coordenadas_list
    }

    # lista = ["coordenadas": coordenadas, "meses": meses]

    # return render(request, "heatMap.html", {"coordenadas": coordenadas, "meses": meses})

    return render(
        request=request, 
        template_name="heatMap.html",
        context=context
    )

def selected(request):
    vmes = request.POST.get("mes")
    meses = Meses.objects.all()
    meses_lista = [[meses[vmes]] for mes in meses]

    context = {
        "meses_list": meses_lista
    }

    return render(
        rquest=request, 
        template_name="heatMap.html",
        context=context)