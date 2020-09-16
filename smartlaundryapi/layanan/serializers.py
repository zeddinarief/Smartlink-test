# Serialize data ke data json
def serializeService(values, user):
    return {
        "code": 200,
        "status": "success",
        "data": {
            "id": values.id_layanan,
            "nama": values.name,
            "unit": values.unit,
            "harga": values.harga,
            "user_id": user
        }
    }