from django.shortcuts import render
from .models import Tienda

# Create your views here.
def ObjetoTienda(request):
    obj = Tienda.objects.all()
    context ={
      'productos': obj
    }
    return render(request, 'objetos/test.html', context)

