from flask import Flask, render_template,request,redirect, url_for,flash
from flask_mysqldb import MySQL
import datetime
import hashlib
import pymysql
import re
import datetime
from datetime import date

app = Flask(__name__)

class UsuarioReg:

    def __init__(self, usuario,contrasena,nombre,apellidos,fecha_nac,correo):
    
        self.usuario = usuario
        self.contrasena = contrasena   
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nac = fecha_nac
        self.correo = correo

    def crearUsuario(self):
        ###############################################

        cifrado = hashlib.md5((self.contrasena).encode('utf-8'))
        if vali_usuario(self) and vali_edad(self):
            consultaPreparada = 'INSERT INTO usuario (usuario, contrasena, nombre, apellido, fecha_nac, correo) VALUES ("{}", "{}", "{}", "{}", "{}", "{}");'.format(self.usuario,cifrado.hexdigest(),self.nombre,self.apellidos,self.fecha_nac,self.correo)
            connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
            cursor = connection.cursor()
            cursor.execute(consultaPreparada)
            connection.commit()
            connection.close()
            return True
        else:
            flash("Nombre de usuario ya registrado")
            return False

        #Valida la edad del usuario
        ###############################################
        def vali_edad(self):
            
            fecha_actual=date.today()
            anio = self.fecha_nac[:4]
            mes = self.fecha_nac[5:7]
            dia = self.fecha_nac[8:10]
            resultado=fecha_actual.year - int(anio)
            resultado -=((fecha_actual.month,fecha_actual.day)< (int(mes),int(dia)))
            if resultado>=18:   
                return True
            else:
                return False


        #Esta funcion valida si el usuario con el que se va a registrar esta ya registrado o no, si lo esta
        #Devuelve False y no le permitira ingresar ,si es True, continuara a agregarUsuario
        ###############################################
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

        
        