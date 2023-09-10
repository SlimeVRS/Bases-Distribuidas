from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://192.168.100.36:27017/bibliotecatec'

mongo = PyMongo(app)

##################################################
#                   Libros                       #
##################################################

@app.route('/libros', methods=['GET'])
def get_books():
    books = mongo.db.libros.find()
    response = json_util.dumps(books)
    return Response(response, mimetype='application/json')

@app.route('/libros/<id>', methods=['GET'])
def get_book(id):
    print(id)
    book = mongo.db.libros.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(book)
    return Response(response, mimetype="application/json")

@app.route('/libros', methods=['POST'])
def create_book():
    # Receiving data
    name = request.json['name']
    author = request.json['author']
    user_rating = request.json['user_rating']
    reviews = request.json['reviews']
    price = request.json['price']
    year = request.json['year']
    genre = request.json['genre']
    estado = request.json['estado']

    if name and author and user_rating and reviews and price and year and genre and estado:
        id = mongo.db.libros.insert_one({
            'name': name, 'author': author, 'user_rating': user_rating, 'reviews': reviews, 'price': price, 'year': year, 'genre': genre, 'estado': estado
        })
        response = {
            '_id' : str(id),
            'name': name,
            'author': author,
            'user_rating': user_rating,
            'reviews': reviews,
            'price': price,
            'year': year,
            'genre': genre,
            'estado': estado
        }
        return response
    else:
        return not_found()

@app.route('/libros/<id>', methods=['PUT'])
def update_book(id):
    name = request.json['name']
    author = request.json['author']
    user_rating = request.json['user_rating']
    reviews = request.json['reviews']
    price = request.json['price']
    year = request.json['year']
    genre = request.json['genre']
    estado = request.json['estado']

    if name and author and user_rating and reviews and price and year and genre and estado:
        mongo.db.libros.update_one({'_id': ObjectId(id)}, {'$set': {
            'name': name,
            'author': author,
            'user_rating': user_rating,
            'reviews': reviews,
            'price': price,
            'year': year,
            'genre': genre,
            'estado': estado
        }})
        response = jsonify({ 'message': 'Book' + id + 'was updated successfuly'})
        return response

@app.route('/libros/<id>', methods=['DELETE'])
def delete_book(id):
    print(id)
    mongo.db.libros.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Book ' + id + 'was deleted successfuly'})
    return response

##################################################
#                   USUARIOS                     #
##################################################

@app.route('/usuarios', methods=['GET'])
def get_users():
    users = mongo.db.usuarios.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/usuarios/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = mongo.db.usuarios.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")

@app.route('/usuarios', methods=['POST'])
def create_user():
    # Receiving data
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    identificacion = request.json['identificacion']
    morosidad = request.json['morosidad']
    rol = request.json['rol']
    alquilerLibro = request.json['alquilerLibro']
    genero = request.json['genero']
    correo = request.json['correo']

    if nombre and apellido and identificacion and morosidad and rol and alquilerLibro and genero and correo:
        id = mongo.db.usuarios.insert_one({
            'nombre': nombre,
            'apellido': apellido,
            'identificacion': identificacion,
            'morosidad': morosidad,
            'rol': rol,
            'alquilerLibro': alquilerLibro,
            'genero': genero,
            'correo': correo
        })
        response = {
            '_id' : str(id),
            'nombre': nombre,
            'apellido': apellido,
            'identificacion': identificacion,
            'morosidad': morosidad,
            'rol': rol,
            'alquilerLibro': alquilerLibro,
            'genero': genero,
            'correo': correo
        }
        return response
    else:
        return not_found()

@app.route('/usuarios/<id>', methods=['PUT'])
def update_user(id):
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    identificacion = request.json['identificacion']
    morosidad = request.json['morosidad']
    rol = request.json['rol']
    alquilerLibro = request.json['alquilerLibro']
    genero = request.json['genero']
    correo = request.json['correo']

    if nombre and apellido and identificacion and morosidad and rol and alquilerLibro and genero and correo:
        mongo.db.usuarios.update_one({'_id': ObjectId(id)}, {'$set': {
            'nombre': nombre,
            'apellido': apellido,
            'identificacion': identificacion,
            'morosidad': morosidad,
            'rol': rol,
            'alquilerLibro': alquilerLibro,
            'genero': genero,
            'correo': correo
        }})
        response = jsonify({ 'message': 'User' + id + 'was updated successfuly'})
        return response

@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_user(id):
    print(id)
    mongo.db.usuarios.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User ' + id + 'was deleted successfuly'})
    return response

##################################################
#                   PRESTAMOS                    #
##################################################

@app.route('/prestamos', methods=['GET'])
def get_loans():
    loans = mongo.db.prestamos.find()
    response = json_util.dumps(loans)
    return Response(response, mimetype='application/json')

@app.route('/prestamos/<id>', methods=['GET'])
def get_loan(id):
    print(id)
    loan = mongo.db.prestamos.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(loan)
    return Response(response, mimetype="application/json")

@app.route('/prestamos', methods=['POST'])
def create_loan():
    # Receiving data
    id_usuario = request.json['id_usuario'],
    id_libro = request.json['id_libro'],
    fecha_alquiler = request.json['fecha_alquiler'],
    fecha_devolucion = request.json['fecha_devolucion'],
    estado = request.json['estado'],
    cobro_retraso = request.json['cobro_retraso']

    if id_usuario and id_libro and fecha_alquiler and fecha_devolucion and estado and cobro_retraso:
        id = mongo.db.prestamos.insert_one({
            'id_usuario': id_usuario,
            'id_libro': id_libro,
            'fecha_alquiler': fecha_alquiler,
            'fecha_devolucion': fecha_devolucion,
            'estado': estado,
            'cobro_retraso': cobro_retraso
        })
        response = {
            '_id' : str(id),
            'id_usuario': id_usuario,
            'id_libro': id_libro,
            'fecha_alquiler': fecha_alquiler,
            'fecha_devolucion': fecha_devolucion,
            'estado': estado,
            'cobro_retraso': cobro_retraso
        }
        return response
    else:
        return not_found()

@app.route('/prestamos/<id>', methods=['PUT'])
def update_loan(id):
    id_usuario = request.json['id_usuario'],
    id_libro = request.json['id_libro'],
    fecha_alquiler = request.json['fecha_alquiler'],
    fecha_devolucion = request.json['fecha_devolucion'],
    estado = request.json['estado'],
    cobro_retraso = request.json['cobro_retraso']

    if id_usuario and id_libro and fecha_alquiler and fecha_devolucion and estado and cobro_retraso:
        mongo.db.prestamos.update_one({'_id': ObjectId(id)}, {'$set': {
            'id_usuario': id_usuario,
            'id_libro': id_libro,
            'fecha_alquiler': fecha_alquiler,
            'fecha_devolucion': fecha_devolucion,
            'estado': estado,
            'cobro_retraso': cobro_retraso
        }})
        response = jsonify({ 'message': 'Loan' + id + 'was updated successfuly'})
        return response

@app.route('/prestamos/<id>', methods=['DELETE'])
def delete_loan(id):
    print(id)
    mongo.db.prestamos.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Loan ' + id + 'was deleted successfuly'})
    return response

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True)