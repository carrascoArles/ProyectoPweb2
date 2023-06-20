from django.shortcuts import render
from .models import Tienda

# Create your views here.
def ObjetoTienda(request):
    obj = Tienda.objects.all()
    categorias = []
    for producto in obj:
        if producto.categoria not in categorias :
            categorias.append(producto.categoria)
    context ={
      'productos': obj,
      'categorias': categorias,
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
