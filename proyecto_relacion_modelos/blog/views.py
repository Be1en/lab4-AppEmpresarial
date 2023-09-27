from django.shortcuts import render
from .models import Entrada, Autor

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def index(request):
    return render(request, 'blog/index.html')

def lista_mario(request):
     # Obtiene el objeto Autor relacionado con el nombre "Mario Vargas Llosa"
    autor_mario_vargas_llosa = Autor.objects.get(nombre="Mario Vargas Llosa")

    # Filtra las entradas por el autor "Mario Vargas Llosa"
    entradas = Entrada.objects.filter(autor=autor_mario_vargas_llosa)

    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def lista_ton(request):
    autor_ton_cruise = Autor.objects.get(nombre="Ton Cruise")
    entradas = Entrada.objects.filter(autor=autor_ton_cruise )
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

