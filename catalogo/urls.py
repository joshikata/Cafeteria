from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),  
    path('cliente/', views.vista_cliente, name='vista_cliente'),  
    path('encargado/', views.vista_encargado, name='vista_encargado'),  
]