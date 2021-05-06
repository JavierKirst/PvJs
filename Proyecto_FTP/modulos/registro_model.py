from flask import Flask, render_template,request,redirect, url_for,flash
from flask_mysqldb import MySQL
import datetime
import hashlib
import pymysql
import re

from datetime import date

def calcular_edad(fecha_nacimiento):

      fecha_actual=date.today()
      resultado=fecha_actual.year -fecha_nacimiento.year
      resultado -=((fecha_actual.month,fecha_actual.day)<(fecha_nacimiento.month,fecha_nacimiento.day))
      if resultado>=18:
       return True
      else:
       return False

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
        cifrada = hashlib.md5((self.contrasena).encode('utf-8'))
        consultaPreparada = 'INSERT INTO usuario (usuario, contrasena, nombre, apellido, fecha_nac, correo) VALUES ("{}", "{}", "{}", "{}", "{}", "{}");'.format(self.usuario,cifrada,self.nombre,self.apellidos,self.fecha_nac,self.correo)
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        cursor.execute(consultaPreparada)
        connection.commit()
        connection.close()

#Valida la edad del usuario
def vali_edad(self):
        
    horaActual = datetime.datetime.now()
    f_nacimiento = self.fecha_nac
    difference_in_years = (horaActual, f_nacimiento).years
    return difference_in_years

    #Valida que el correo introducido sea un correo valido

def es_correo_valido(self): 

    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, self.correo) is not None

#Esta funcion valida si el usuario con el que se va a registrar esta ya registrado o no, si lo esta
#Devuelve False y no le permitira ingresar ,si es True, continuara a agregarUsuario
def vali_usuario(self):
    preparada = ('Select usuario from usuario where usuario = {}'.format(self.usuario))
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
    cursor = connection.cursor()
    cursor.execute(preparada)
    data = cursor.fetchall()
    connection.commit()
    connection.close()

    if data == 0 or data is None:
        return True
    else:
        return False



#Funciona para editar los datos del usuario
def editarUsuario(self):
    pass
