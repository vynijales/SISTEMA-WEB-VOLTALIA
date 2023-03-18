from django.shortcuts import render, redirect
from .models import Coordenadas, Meses
import json

# Create your views here.

def heatMap(request):
    vmes = "janeiro21"
    
    coordenadas = Coordenadas.objects.all()
    meses = Meses.objects.all()
    # print(request)
    coordenadas_list = [[float(coord.longitude), float(coord.latitude)] for coord in coordenadas]
    
    lista = []
    for coord, mes in zip(coordenadas, meses):
        lista.append([float(coord.latitude), float(coord.longitude)])

    # lista = ["coordenadas": coordenadas, "meses": meses]

    # return render(request, "heatMap.html", {"coordenadas": coordenadas, "meses": meses})

    abc = ["janeiro21", "fevereiro21", "marco21", "abril21", "maio21", "junho21", "julho21", "agosto21", "setembro21", "outubro21", "novembro21", "dezembro21", "janeiro22"]

    if request.method == 'POST':
        vmes = request.POST.get("mes")
        print(vmes)
        meses = Meses.objects.all()
        if vmes == "janeiro21":
            meses_lista = [float(mes.janeiro21) for mes in meses]
            
        elif vmes == "fevereiro21":
            meses_lista = [float(mes.fevereiro21) for mes in meses]
        elif vmes == "marco21":
            meses_lista = [float(mes.marco21) for mes in meses]
        elif vmes == "abril21":
            meses_lista = [float(mes.abril21) for mes in meses]
        elif vmes == "marco21":
            meses_lista = [float(mes.marco21) for mes in meses]
        elif vmes == "abril21":
            meses_lista = [float(mes.abril21) for mes in meses]
    else:
        meses_lista = [float(mes.janeiro21) for mes in meses]
    context = {
        "coordenadas": coordenadas,
        "meses": meses,
        # "coordenadas_json": json.dumps(coordenadas_list),
        "coordenadas_list": coordenadas_list,
        "weights": meses_lista,
        "vmes": vmes,
    }

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