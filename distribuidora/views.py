from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def resumen_dashboard(request):
    return render(request, 'dashboard/resumen.html')