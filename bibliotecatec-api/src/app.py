from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime, timedelta

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors


app = Flask(__name__)
app.config['MONGO_URI']='mongodb://192.168.100.36:27017/bibliotecatec'

# Swagger configs

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "BibliotecaTEC API"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

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
def get_book_by_id(id):
    print(id)
    book = mongo.db.libros.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(book)
    return Response(response, mimetype="application/json")

@app.route('/librosnombre/<name>', methods=['GET'])
def get_book_by_name(name):
    book = mongo.db.libros.find({'name': name})
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
    user = mongo.db.usuarios.find_one({'_id': id})
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")

@app.route('/usuarios', methods=['POST'])
def create_user():
    # Receiving data
    _id = request.json['_id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    ubicacion = request.json['ubicacion']
    morosidad = request.json['morosidad']
    rol = request.json['rol']
    alquilerLibro = request.json['alquilerLibro']
    genero = request.json['genero']
    correo = request.json['correo']

    if _id and nombre and apellido and ubicacion and morosidad and rol and alquilerLibro and genero and correo:
        id = mongo.db.usuarios.insert_one({
            '_id': _id,
            'nombre': nombre,
            'apellido': apellido,
            'morosidad': morosidad,
            'ubicacion': ubicacion,
            'rol': rol,
            'alquilerLibro': alquilerLibro,
            'genero': genero,
            'correo': correo
        })
        response = {
            '_id' : str(id),
            'nombre': nombre,
            'apellido': apellido,
            'ubicacion': ubicacion,
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
    _id = request.json['_id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    morosidad = request.json['morosidad']
    ubicacion = request.json['ubicacion']
    rol = request.json['rol']
    alquilerLibro = request.json['alquilerLibro']
    genero = request.json['genero']
    correo = request.json['correo']

    if _id and nombre and apellido and ubicacion and morosidad and rol and alquilerLibro and genero and correo:
        mongo.db.usuarios.update_one({'_id': id}, {'$set': {
            '_id': _id,
            'nombre': nombre,
            'apellido': apellido,
            'morosidad': morosidad,
            'ubicacion': ubicacion,
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
    mongo.db.usuarios.delete_one({'_id': id})
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

@app.route('/usuariosmorosos', methods=['GET'])
def get_defaulter_users():
    loans = mongo.db.prestamos.find({'estado': 'atrasado'})
    temp = loans
    generate_pdf(temp)
    response = json_util.dumps(loans)
    return Response(response, mimetype='application/json')

def generate_pdf(defaulters):
    relation_defaulter = [["Carne", "Cobro"]]
    formato = "%Y-%m-%d %H:%M:%S.%f"
    for i in defaulters:
        temp = []
        fecha = datetime.strptime(i['fecha_devolucion'], formato)
        cobro = ((datetime.now() - fecha).days // 7) * 2000
        temp.append(i['id_usuario'])
        temp.append(cobro)
        relation_defaulter.append(temp)
    
    fileName = 'Cobros.pdf'
    pdf = SimpleDocTemplate(
        fileName,
        pagesize=letter
    )
    
    table = Table(relation_defaulter)
    
    style = TableStyle([
        ('BACKGROUND', (0,0), (1,0), colors.green),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),

        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 14),

        ('BOTTOMPADDING', (0,0), (-1,0), 12),

        ('BACKGROUND', (0,1), (-1,-1), colors.beige),      
    ])
    table.setStyle(style)
    rowNumb = len(relation_defaulter)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.burlywood
        else:
            bc = colors.beige
        ts = TableStyle([
            ('BACKGROUND', (0, i), (-1,i), bc)
        ])
        table.setStyle(ts)
    
    ts = TableStyle([
        ('BOX', (0,0), (-1,-1),2,colors.black),
        ('GRID', (0,1),(-1,-1),2,colors.black)
    ])
    table.setStyle(ts)


    elems = []
    elems.append(table)

    pdf.build(elems)


@app.route('/prestamos', methods=['POST'])
def create_loan():
    # Receiving data
    id_usuario = request.json['id_usuario'],
    id_libro = request.json['id_libro'],
    estado = request.json['estado'],
    cobro_retraso = request.json['cobro_retraso']

    fecha_alquiler = datetime.now()
    fecha_devolucion = str(fecha_alquiler + timedelta(days=15))

    fecha_alquiler = str(datetime.now())

    print(type(fecha_alquiler), type(fecha_devolucion))

    if id_usuario and id_libro and estado and cobro_retraso:
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