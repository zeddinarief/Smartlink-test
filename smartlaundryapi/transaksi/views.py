from smartlaundryapi.response import Response
from . import serializers
from .models import Transactions, Detail
from layanan.models import Services
from userauth.models import Users
import json
from django.contrib.auth.hashers import make_password, check_password
from smartlaundryapi.middleware import jwtRequired
from smartlaundryapi.jwt import JWTAuth

# Create your views here.
@jwtRequired
def insertTransaction(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        # membuat id transaksi
        old_transaction = Transactions.objects.all().last()
        new_id = 0
        if not old_transaction:
            new_id = 1
        else:
            new_id = int(old_transaction.id_transaction[3:]) + 1

        new_id = "TRX" + str(new_id).zfill(3)

        # insert ke database
        transaction = Transactions()
        transaction.id_transaction = new_id
        transaction.pelanggan = json_data['pelanggan']

        total = 0
        for x in json_data['layanan']:
            layanan_id = x['id_layanan'].upper()
            qty = x['qty']
            service = Services.objects.filter(id_layanan=layanan_id).first()

            if not service:
                return Response.badRequest(values={"message": "Layanan yang anda masukkan tidak terdaftar!"})        

            # hitung total tagihan sebelum diskon
            total += service.harga * qty

        # menambahkan data total dan persen diskon pada objek transaksi
        transaction.total = total
        transaction.diskon_persen = json_data['diskon_persen']
        
        # Menghitung diskon rupiah dan menambahkan data pada objek transaksi
        diskon_rupiah = total * int(json_data['diskon_persen'])/100
        transaction.diskon_rupiah = diskon_rupiah

        # Menghitung tagihan dan menambahkan data pada objek transaksi
        transaction.tagihan = total - diskon_rupiah

        user = Users.objects.filter(id=request.session['user_id']).first()
        transaction.user = user

        # Simpan data dalam database
        transaction.save()
        
        # Data array detail transaksi
        detail = insertDetail(json_data['layanan'], new_id)

        # Convert data objek menjadi data Json
        response = serializers.serializeTransaction(transaction, detail, transaction.user.id_user)
        
        # Buat dan kirim pesan respon pada client
        return Response.ok(values=response)
    else:
        return Response.badRequest(values={"message": "Method yang anda masukkan salah"})

# Menambahkan data detail ke database
def insertDetail(layanan, idTransaction):
    arr = []
    for x in layanan:
        detail = Detail()
        detail.qty = x['qty']

        # Get data transaksi dari database berdasarkan id transaksi dan menambahkan pada objek detail
        transaction = Transactions.objects.filter(id_transaction=idTransaction).first()
        detail.transaction = transaction

        # Get data layanan dari database berdasarkan id layanan dan menambahkan pada objek detail
        layanan_id = x['id_layanan'].upper()
        service = Services.objects.filter(id_layanan=layanan_id).first()
        detail.layanan = service

        detail.save()
        arr.append(detail)

    print('detail method', arr)
    return arr