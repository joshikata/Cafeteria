from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings



class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    activa = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        
        if Producto.objects.filter(categoria=self).exists():
            raise ValidationError("No se puede eliminar una categoría que tiene productos asociados.")
        super().delete(*args, **kwargs)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
       
        if Categoria.objects.filter(id=self.categoria.id).exists():
            raise ValidationError("No se puede eliminar un producto asociado a una categoría.")
        super().delete(*args, **kwargs)


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=150)  
    fecha = models.DateTimeField(auto_now_add=True)
    hora_retiro = models.TimeField()
    estado = models.CharField(max_length=15)
    total = models.IntegerField()
    observaciones = models.TextField()


class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    subtotal = models.IntegerField()