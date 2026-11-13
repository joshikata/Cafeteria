from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, DetallePedido, Pedido, Categoria, User

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

