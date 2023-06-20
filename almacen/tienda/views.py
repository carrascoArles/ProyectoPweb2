from django.shortcuts import render
from .models import Tienda

# Create your views here.
def ObjetoTienda(request):
    obj = Tienda.objects.all()
    context ={
      'productos': obj
    }
    return render(request, 'objetos/test.html', context)

def obtener_productos(request):
    categoria = request.GET.get('categoria')
    if categoria == 'Todos':
        productos = Tienda.objects.all()
    else:
        productos = Tienda.objects.filter(categoria=categoria)
    context = {
        'productos': productos
    }
    return render(request, 'objetos/test_productos.html', context)