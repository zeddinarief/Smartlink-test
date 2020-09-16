from smartlaundryapi.response import Response
from . import serializers
from .models import Users
import json
from django.contrib.auth.hashers import make_password, check_password
from smartlaundryapi.middleware import jwtRequired
from smartlaundryapi.jwt import JWTAuth

def register(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data['username']

        user_check = Users.objects.filter(username=username).first()

        # cek apakah user sudah terdaftar
        if user_check:
            return Response.badRequest(values={"message": "Gagal! Pengguna telah terdaftar!"})

        # membuat id unik user
        old_user = Users.objects.all().last()
        new_id = 0

        if not old_user:
            new_id = 1
        else:
            new_id = int(old_user.id_user[3:]) + 1

        new_id = "USR" + str(new_id).zfill(3)

        # menambahkan data ke class model users
        user = Users()
        user.id_user = new_id
        user.name = json_data['nama']
        user.username = json_data['username']
        user.password = make_password(password=json_data['password'])
        user.telepon = json_data['telepon']

        # simpan data pada database
        user.save()

        # Convert data objek menjadi data Json
        response = serializers.serializeRegister()

        # Buat dan kirim pesan respon pada client
        return Response.ok(values=response)
    else:
        return Response.badRequest(values={"message": "Method yang anda masukkan salah"})

def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = json_data['username']

        user = Users.objects.filter(username=username).first()

        # cek apakah username sudah terdaftar
        if not user:
            return Response.badRequest(values={"message": "Pengguna belum terdaftar!"})

        # cek kecocokan password
        if not check_password(json_data['password'], user.password):
            return Response.badRequest(values={"message": "Password yang kamu masukkan salah!"})

        # simpan id user pada session
        request.session['user_id'] = user.id

        # generate auth token menggunakan jwt auth token
        jwt = JWTAuth()
        token = jwt.encode({"id": user.id_user})

        # Convert data objek menjadi data Json
        user = serializers.serializeLogin(user, token)

        # Buat dan kirim pesan respon pada client
        return Response.ok(values=user)

    else:
        return Response.badRequest(values={"message": "Method yang anda masukkan salah"})