from django.db import models
from pyexpat import model
# Create your models here.


class makanan(models.Model):
        nama = models.CharField(max_length= 45)
        asal = models.CharField(max_length= 45)
        gambar = models.ImageField(upload_to = 'makanan')
        def __str__(self):
            return self.nama