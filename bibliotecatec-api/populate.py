from pymongo import MongoClient
import json

MONGO_URI = 'mongodb://192.168.100.36:27017'

client = MongoClient(MONGO_URI)

db = client['bibliotecatec']
libros = db['libros']
usuarios = db['usuarios']
prestamos = db['prestamos']

h = open('F:\\Progras\\Bases-Distribuidas\\bibliotecatec-api\\Prestamos.json', encoding="utf8")
data = json.load(h)

for i in data:
    prestamos.insert_one({
                        "id_usuario": i['id_usuario'],
                        "id_libro": i['id_libro'],
                        "fecha_alquiler": i['fecha_alquiler'],
                        "fecha_devolucion":	i['fecha_devolucion'],
                        "estado": i['estado'],
                        "cobro_retraso": i['cobro_retraso']
                        })

h.close()
"""
f = open('F:\\Progras\\Bases-Distribuidas\\bibliotecatec-api\\bsamazon.json', encoding= "utf8")
data = json.load(f)

g = open('F:\\Progras\\Bases-Distribuidas\\bibliotecatec-api\\usuarios.json', encoding="utf8")
data1 = json.load(g)

for i in data:
    libros.insert_one({
                            "name": i['Name'],
                            "author": i['Author'],
                            "user_rating": i['User Rating'],
                            "reviews": i['Reviews'],
                            "price": i['Price'],
                            "year": i['Year'],
                            "genre": i['Genre'],
                            "estado": i['estado']
                            })

for j in data1:
    usuarios.insert_one({
        "_id": i['id'],
        "nombre": i['nombre'],
        "apellido": i['apellido'],
        "morosidad": i['morosidad'],
        "rol": i['rol'],
        "alquilerLibro": i['alquilerLibro'],
        "genero": i['genero'],
        "correo": i['correo']
    })

f.close()"""