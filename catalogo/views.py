from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, DetallePedido, Pedido, Categoria
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def encargado_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Acceso denegado: Solo para encargados.")
        return view_func(request, *args, **kwargs)
    return login_required(_wrapped_view)

@encargado_required
def vista_encargado(request):
    return render(request, 'encargado.html')

@login_required
def vista_cliente(request):
    return render(request, 'cliente.html')

