from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import (
    Http404,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from allauth.account.decorators import verified_email_required
from fortnite_apps.sistema.models import Perfil
from django.contrib.auth.models import User


def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')

def reglas(request):
    #return HttpResponse('homepage')
    return render(request, 'reglas.html')

def premios(request):
    #return HttpResponse('homepage')
    return render(request, 'premios.html')

def blackpan(request):
    #return HttpResponse('homepage')
    return render(request, 'black_pan/principal.html')

def blackpan_participantes(request):
    #return HttpResponse('homepage')
    return render(request, 'black_pan/participantes.html')

def blackpan_resultados(request):
    userobjectpc = Perfil.objects.filter(user__last_name='psn', VERIFICACION_2=True, blackpan='SI').order_by('-puntos')
    return render(request, 'black_pan/resultados.html', {'participantes': userobjectpc})

def blackpan_premios(request):
    #return HttpResponse('homepage')
    return render(request, 'black_pan/premios.html')

def blackpan_terminos(request):
    #return HttpResponse('homepage')
    return render(request, 'black_pan/terminos.html')
