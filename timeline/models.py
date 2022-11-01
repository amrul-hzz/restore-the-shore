from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JoinEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    namaEvent = models.CharField(max_length = 255)
    namaPantai = models.CharField(max_length = 255)
    alamatPantai = models.CharField(max_length = 255)
    jumlahPartisipan = models.IntegerField()
    fotoPantai = models.URLField()
    deskripsi = models.TextField()
    tanggalMulai = models.DateField()
    tanggalAkhir = models.DateField()
    
