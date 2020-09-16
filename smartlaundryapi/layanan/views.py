from smartlaundryapi.response import Response
from . import serializers
from .models import Services
from userauth.models import Users
import json
from django.contrib.auth.hashers import make_password, check_password
from smartlaundryapi.middleware import jwtRequired
from smartlaundryapi.jwt import JWTAuth

# Create your views here.
@jwtRequired
def insertService(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        nama = json_data['nama']
        
        service_check = Services.objects.filter(name=nama).first()
        
        # Cek apakah layanan sudah terdaftar
        if service_check:
            return Response.badRequest(values={"message": "Gagal! Layanan sudah terdaftar!"})

        # membuat id layanan
        old_service = Services.objects.all().last()
        new_id = 0
        if not old_service:
            new_id = 1
        else:
            new_id = int(old_service.id_layanan[3:]) + 1

        new_id = "LYN" + str(new_id).zfill(3)

        # menambahkan data ke class model service
        service = Services()
        service.id_layanan = new_id
        service.name = json_data['nama']
        service.unit = json_data['unit']
        service.harga = json_data['harga']

        user = Users.objects.filter(id=request.session['user_id']).first()
        service.user = user

        # simpan data service ke database
        service.save()

        # ubah data objek ke data json
        response = serializers.serializeService(service, service.user.id_user)

        # Buat dan kirim pesan respon pada client
        return Response.ok(values=response)
    else:
        return Response.badRequest(values={"message": "Method yang anda masukkan salah"})