from django.db import models
from layanan.models import Services
from userauth.models import Users

# Model tabel transactions
class Transactions(models.Model):
    id_transaction = models.CharField(max_length=6, unique=True)
    pelanggan = models.CharField(max_length=200)
    total = models.BigIntegerField()
    diskon_persen = models.IntegerField()
    diskon_rupiah = models.BigIntegerField()
    tagihan = models.BigIntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'transactions'

# Model tabel transaction_detail
class Detail(models.Model):
    qty = models.IntegerField()
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    layanan = models.ForeignKey(Services, on_delete=models.CASCADE)

    class Meta:
        db_table = 'transaction_detail'