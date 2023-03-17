from django.shortcuts import render, redirect

# Create your views here.

def heatMap(request):
    return render(request, "heatMap.html")