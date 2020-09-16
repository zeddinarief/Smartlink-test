from django.db import models
from userauth.models import Users

# Model tabel services
class Services(models.Model):
    id_layanan = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=20)
    harga = models.BigIntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'services'