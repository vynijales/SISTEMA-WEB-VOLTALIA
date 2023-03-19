from django.shortcuts import render, redirect
from .models import Coordenadas, Meses
import json

def heatMap(request):
    vmes = "janeiro21"
    coordenadas = Coordenadas.objects.all()
    meses = Meses.objects.all()
    coordenadas_list = [[float(coord.longitude), float(coord.latitude), coord.id] for coord in coordenadas]
    meses_lista = []

    if request.method == 'POST':
        vmes = request.POST.get("mes")
        meses = Meses.objects.all()
        if vmes == "janeiro21":
            meses_lista = [float(mes.janeiro21) for mes in meses]
        elif vmes == "fevereiro21":
            meses_lista = [float(mes.fevereiro21) for mes in meses]
        elif vmes == "marco21":
            meses_lista = [float(mes.marco21) for mes in meses]
        elif vmes == "abril21":
            meses_lista = [float(mes.abril21) for mes in meses]
        elif vmes == "maio21":
            meses_lista = [float(mes.maio21) for mes in meses]
        elif vmes == "junho21":
            meses_lista = [float(mes.junho21) for mes in meses]
        elif vmes == "julho21":
            meses_lista = [float(mes.julho21) for mes in meses]
        elif vmes == "agosto21":
            meses_lista = [float(mes.agosto21) for mes in meses]
        elif vmes == "setembro21":
            meses_lista = [float(mes.setembro21) for mes in meses]
        elif vmes == "outubro21":
            meses_lista = [float(mes.outubro21) for mes in meses]
        elif vmes == "novembro21":
            meses_lista = [float(mes.novembro21) for mes in meses]
        elif vmes == "dezembro21":
            meses_lista = [float(mes.dezembro21) for mes in meses]
        elif vmes == "janeiro22":
            meses_lista = [float(mes.janeiro22) for mes in meses]
    else:
        meses_lista = [float(mes.janeiro21) for mes in meses]
        
    valores = [
            {'valor': 'janeiro21', 'nome': 'Janeiro 2021'},
            {'valor': 'fevereiro21', 'nome': 'Fevereiro 2021'},
            {'valor': 'marco21', 'nome': 'Março 2021'},
            {'valor': 'abril21', 'nome': 'Abril 2021'},
            {'valor': 'maio21', 'nome': 'Maio 2021'},
            {'valor': 'junho21', 'nome': 'Junho 2021'},
            {'valor': 'julho21', 'nome': 'Julho 2021'},
            {'valor': 'agosto21', 'nome': 'Agosto 2021'},
            {'valor': 'setembro21', 'nome': 'Setembro 2021'},
            {'valor': 'outubro21', 'nome': 'Outubro 2021'},
            {'valor': 'novembro21', 'nome': 'Novembro 2021'},
            {'valor': 'dezembro21', 'nome': 'Dezembro 2021'},
            {'valor': 'janeiro22', 'nome': 'Janeiro 2022'},
        ]
    
    context = {
        "coordenadas_list": coordenadas_list,
        "meses_lista": meses_lista,
        "vmes": vmes,
        "lista": valores,
    }

    return render(
        request=request, 
        template_name="heatMap.html",
        context=context
    )

