# global
# Imports
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import os
from modulos.usuario import *
from flask import Flask, session
from modulos import usuario
from modulos import registro_model
from modulos import seguidores_model
from modulos import publicacion_model

app = Flask(__name__)

app.secret_key = 'esto-es-una-clave-muy-secreta'

# CREA SESSION

@app.before_request
def session_management():
    session.permanent = True

#REDIRECCION LOGIN

@app.route('/login')
def log_view():
    return render_template("login.html")

#REDIRECCION REGISTRO

@app.route('/registro')
def registro():
    return render_template("registro.html")

# CONECTARSE A LA CUENTA

@app.route('/main', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        obj_Usuario = UsuarioLog(usuario)
        datosUsuario = obj_Usuario.conectarUsuario(contrasena) 
        if len(datosUsuario)!=0:
        #Guarda los datos necesarios del usuario que son publicos para los demas seguidores o usuarios
            session['usuario'] = usuario
            session['coduser'] = datosUsuario[0]
            session['fecha_nac'] = datosUsuario[5]
            session['nombre'] = datosUsuario[3]
            session['biografia'] = datosUsuario[-2]
            session['foto'] = datosUsuario[-1]
            flash("Bienvenido!!")
            return render_template('main.html')
        else:
            flash("Intentelo de nuevo")
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

# DESCONECTARSE DE LA CUENTA

@app.route('/desc')
def desc():
    session.clear()
    return render_template('login.html')

# IR AL MENU DE CONFIGURACION

@app.route('/config')
def config():
    try:
        if session['usuario']:
            return render_template('config.html')
    except:
        return redirect(url_for('login'))


# CREAR NUEVA CUENTA/USUARIO
@app.route('/add_user', methods=['POST'])
def nuevoUsuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        fecha_nac = request.form['fecha_nac']
        correo = request.form['correo']
        obj_Usuario_nuevo = registro_model.UsuarioReg(usuario, contrasena, nombre, apellidos, fecha_nac, correo)
    #Si lo crea el usuario
        if obj_Usuario_nuevo.crearUsuario():
    #Si se conecta
            if login():
                return render_template('main.html') 
    #Si no crea el usuario
        else:
            return redirect(url_for('registro'))

@app.route('/',methods=['POST'])
def interaccionMain():
    if request.method == 'POST':
        if request.form['like']:
            pass# sera con un input 
    pass

#control ir al main si hay usuario conectado
@app.route('/')
def index():
    try:
        if session['usuario']:
            return render_template('main.html')
    except:
        return redirect(url_for('login'))

@app.route('/perfil')
def perfil():
    try:
        if session['usuario']:
            
            obj_Seguidores = seguidores_model.Seguidores(session['coduser'])
            seguidores = obj_Seguidores.mostrarSeguidores()
            seguidos = obj_Seguidores.mostrarSeguidos()
            
            obj_Publicaciones = publicacion_model.Publicacion(session['coduser'])
            publicaciones = obj_Publicaciones.mostrarPublicacionPerfil()
            
            return render_template('perfil.html',numFotos = len(publicaciones),nseguidores=(len(seguidores)),nseguidos=(len(seguidos)),publicaciones=publicaciones)
    except:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)
