# Serialize data ke data json
def serializeTransaction(values, detail, user):
    detail_trx = serializeArray(detail)
    return serializeAll(values, detail_trx, user)

def serializeAll(values, detail, user):
    return {
        "code": 200,
        "status": "success",
        "data": {
            "id": values.id_transaction,
            "pelanggan": values.pelanggan,
            "total": values.total,
            "diskon_persen": values.diskon_persen,
            "diskon_rupiah": values.diskon_rupiah,
            "tagihan": values.tagihan,
            "user_id": user,
            "detail": detail
        }
    }

def serializeArray(values):
    print('serialArray', values)
    arr = []

    for item in values:
        arr.append(serializeDetail(item))

    return arr

def serializeDetail(values):
    return {
        "id": values.id,
        "qty": values.qty,
        "layanan": {
            "layanan_id": values.layanan.id_layanan,
            "nama": values.layanan.name,
            "unit": values.layanan.unit,
            "harga": values.layanan.harga
        }
    }