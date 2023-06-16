from django.shortcuts import render
from .models import Tienda

# Create your views here.
def ObjetoTienda(request):
    obj = Tienda.objects.get(id = 1)
    context ={
      'nombre': obj.nombre,
      'precio': obj.precio,
    }
    return render(request, 'objetos/test.html', context)

