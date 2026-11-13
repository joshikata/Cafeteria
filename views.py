from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# ...existing code...

@login_required
@user_passes_test(lambda u: u.is_staff)
def encargado_view(request):
    # Vista exclusiva para encargados
    return render(request, 'encargado.html')

@login_required
@user_passes_test(lambda u: not u.is_staff)
def cliente_view(request):
    # Vista exclusiva para clientes
    return render(request, 'cliente.html')
# ...existing code...
