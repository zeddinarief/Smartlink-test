# Serialize data ke data json
def serializeRegister():
    return {
        "code": 200,
        "status": "success",
        "message": "Berhasil terdaftar!"
    }

def serializeLogin(values, token):
    return {
        "code": 200,
        "status": "success",
        "data": {
            "id": values.id_user,
            "nama": values.name,
            "username": values.username,
            "token": token
        }
    }