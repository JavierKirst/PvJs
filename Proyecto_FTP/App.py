#global
#Imports
from flask import Flask, render_template,request,redirect, url_for,flash,session
from flask_mysqldb import MySQL
import os
from modulos.usuario import *
from flask import Flask, session
from modulos import usuario
from modulos import registro_model


app = Flask(__name__)

app.secret_key ='esto-es-una-clave-muy-secreta'

'''
@app.route('/datos-sesion',methods=['GET'])
def datos_sesion():
    if 'nombre' in session:
        nombre = session['nombre']
    else:
        nombre = ''
    if 'apellido' in session:
        apellido = session['apellido']
    else:
        apellido = ''
    return 'Datos Sesion: ' + nombre + ' ' + apellido
'''
####################################### CREA SESSION
@app.before_request
def session_management():
    session.permanent = True

####################################### CONECTARSE A LA CUENTA

@app.route('/main',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        obj_Usuario = UsuarioLog(usuario,contrasena)
        if obj_Usuario.conectarUsuario():
            session['usuario'] = usuario
            flash("Bienvenido!!")
            return render_template('main.html')
        else:
            flash("Intentelo de nuevo")
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

####################################### DESCONECTARSE DE LA CUENTA

@app.route('/desc')
def desc():
    session.clear()
    return render_template('login.html')


####################################### CREAR NUEVA CUENTA/USUARIO
@app.route('/add_user', methods=['POST'])
def nuevoUsuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        fecha_nac = request.form['fecha_nac']
        correo = request.form['correo']
        obj_Usuario_nuevo = registro_model.UsuarioReg(usuario,contrasena,nombre,apellidos,fecha_nac,correo)
        obj_Usuario_nuevo.crearUsuario()
    return render_template('main.html')

@app.route('/')
def index():
    if session.permanent:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/login')
def log_view():  
    return render_template("login.html")

@app.route('/registro')
def registro():
    return render_template("registro.html")

if __name__ == '__main__':
    app.run(port=3000, debug=True)