from django.db import models

# Create your models here.
class lugar(models.Model):
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='imagenes')
    descripcion = models.TextField()


class place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self):
        return self.name


