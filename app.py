from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hola mundo"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f"Muchos saludos {nombre}"

@app.route("/verificar-edad/<int:edad>")
def verificar_edad(edad):
    return f"Tienes {edad} a;os"

@app.route("/users", methods=['POST', 'GET'])
def store_user():
    return 'Se guardo el usuario'

@app.post('/address')
def store_addres():
    return "Direccion Guardada"

@app.put('/users')
def update_user():
    return{
        'name': request.form['name'],
        'age': request.form['age'],
        'method': request.method
    }

@app.errorhandler(404)
def not_found(error):
    return 'Ups,esta pagina no existe'




