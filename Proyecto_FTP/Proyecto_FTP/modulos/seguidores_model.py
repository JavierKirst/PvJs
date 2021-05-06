from flask import Flask, render_template,request,redirect, url_for,flash
from flask_mysqldb import MySQL
import hashlib
import pymysql

app = Flask(__name__)

class Seguidores:
    
    def __init__(self,usu_seg):
        self.usu_seg = usu_seg
        
    
    def seguir(self,seguido):
        #session['usuario'] = self.seguidores
        preparada = 'Insert into seguimiento values ("{}","{}");'.format(self.usu_seg,seguido)
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        cursor.execute(preparada)
        connection.commit()
        connection.close()

    def dejarSeguir(self,seguido):
        preparada = 'Delete from seguimiento where seguidores = "{}" and seguidos = "{}";'.format(self.usu_seg,seguido)
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        cursor.execute(preparada)
        connection.commit()
        connection.close()

    def mostrarSeguidores(self):
        preparada = 'Select seguidores from seguimiento where seguidos = "{}"'.format(self.usu_seg)
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        cursor.execute(preparada)
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        return data

    def mostrarSeguidos(self):
        preparada = 'Select seguidos from seguimiento where seguidores = "{}"'.format(self.usu_seg)
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        cursor.execute(preparada)
        data = cursor.fetchall()
        connection.commit()    
        connection.close()
        return data


    def mostrarTodosUsuarios(self,usuariobuscar):
        preparada = 'Select usuario from usuario where usuario like "%{}%"'.format(usuariobuscar)
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        cursor.execute(preparada)
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        return data