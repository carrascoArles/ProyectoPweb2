"""
URL configuration for almacen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import myHomeView
from tienda.views import ObjetoTienda
from tienda.views import obtener_productos

urlpatterns = [
    path('', myHomeView, name='Página de inicio'),
    path('admin/', admin.site.urls),
    path('tienda/',ObjetoTienda,name='otro'),
    path('obtener_productos/',obtener_productos, name='productos'),
]