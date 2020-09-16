from django.db import models

# Model tabel users
class Users(models.Model):
    id_user = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200, null=False)
    telepon = models.CharField(max_length=13, null=False)

    class Meta:
        db_table = 'users'