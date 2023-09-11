from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime, timedelta

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://192.168.100.38:27017/bibliotecatec'

# Swagger configs

SWAGGER_URL = '/swagger'
API_URL = '/static/cobro_swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "Cobro de BibliotecaTEC API"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

mongo = PyMongo(app)

def get_date():
    date_and_time = datetime.now()
    date = date_and_time.strftime("%Y-%m-%d")
    return date

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
    date_style = getSampleStyleSheet()["Normal"]
    date_style.alignment  = 1

    date = get_date()
    paragraph = Paragraph(date, date_style)
    elems.append(paragraph)
    elems.append(table)

    pdf.build(elems)

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