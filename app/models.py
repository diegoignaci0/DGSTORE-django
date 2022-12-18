from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

class Nike(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

class Adidas(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre
        
class Puma(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

    

