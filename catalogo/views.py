from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, DetallePedido, Pedido, Categoria
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.shortcuts import render
from .models import Producto, Categoria


def index(request):
    busqueda = request.GET.get('q', '').strip()
    categoria_id = request.GET.get('categoria', '').strip()

    categorias = Categoria.objects.filter(
        activa=True
    ).order_by('nombre')

    productos = Producto.objects.filter(
        categoria__activa=True
    ).select_related('categoria').order_by('nombre')

    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    categoria_seleccionada = ''

    if categoria_id.isdecimal():
        categoria = categorias.filter(pk=int(categoria_id)).first()

        if categoria:
            productos = productos.filter(categoria=categoria)
            categoria_seleccionada = str(categoria.pk)

    for producto in productos:
        producto.precio_clp = (
            f"${producto.precio:,.0f}".replace(',', '.')
        )

    return render(request, 'index.html', {
        'productos': productos,
        'categorias': categorias,
        'busqueda': busqueda,
        'categoria_seleccionada': categoria_seleccionada,
    })

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

