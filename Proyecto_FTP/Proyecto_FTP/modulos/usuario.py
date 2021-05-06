from flask import Flask, render_template,request,redirect, url_for,flash
from flask_mysqldb import MySQL
from flask import Flask, session
import hashlib
import pymysql
from datetime import date

app = Flask(__name__)

class UsuarioLog:
  
  def __init__(self, usuario):
        
    self.usuario = usuario
    
  def conectarUsuario(self,contrasena):  
    cifrado = hashlib.md5((contrasena).encode('utf-8'))
    preparada = 'Select * from usuario where usuario = "{}" and contrasena = "{}";'.format(self.usuario,cifrado.hexdigest())
    #database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
    cursor = connection.cursor()
    cursor.execute(preparada)
    # some other statements  with the help of cursor
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    if len(rows) != 0:
      return rows[0]
    else: 
      return False

    #Funciona para editar los datos del usuario
    def editarUsuario(self,nombre,apellidos,fecha_nac,correo,biografia,foto):
        cifrado = hashlib.md5((self.contrasena).encode('utf-8'))
        if vali_usuario(self.usuario) and vali_edad(fecha_nac):
            consultaPreparada = 'UPDATE usuario set usuario = "{}", nombre = "{}", apellido = "{}", fecha_nac = "{}",correo = "{}", biografia = "{}",correo = "{}" where usuario = "{}";'.format(self.usuario,nombre,apellidos,fecha_nac,correo,biografia,correo,self.usuario)
            connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
            cursor = connection.cursor()
            cursor.execute(consultaPreparada)
            connection.commit()
            connection.close()


    def editarUsuarioContrasena(self,contrasena):
          cifrado = hashlib.md5((contrasena).encode('utf-8'))
          consultaPreparada = 'UPDATE usuario SET contrasena = "{}" WHERE usuario = "{}"'.format(cifrado,self.usuario)
          connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
          cursor = connection.cursor()
          cursor.execute(consultaPreparada)
          connection.commit()
          connection.close()

    def vali_edad(self,fecha_nac):
          
        fecha_actual=date.today()
        anio = fecha_nac[:4]
        mes = fecha_nac[5:7]
        dia = fecha_nac[8:10]
        resultado=fecha_actual.year - int(anio)
        resultado -=((fecha_actual.month,fecha_actual.day) < (int(mes),int(dia)))
        if resultado>=18:   
            return True
        else:
            return False

    def vali_usuario(self):
        preparada = ('Select usuario from usuario where usuario = "{}"'.format(self.usuario))
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        cursor.execute(preparada)
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        print(data)
        if len(data) == 0:
            return True
        else:
            return False
