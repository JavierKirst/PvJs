from flask import Flask, render_template,request,redirect, url_for,flash
from flask_mysqldb import MySQL
import datetime
import hashlib
import pymysql
import re
import datetime
from datetime import date

app = Flask(__name__)

class Publicacion:

    def __init__(self,cod_usu):
        self.cod_usu = cod_usu

    def subirPublicacion(self,usuario,foto,descripcion):
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        consulta_cod_usu = 'Select cod_usu from usuario where usuario = "{}"'.format(usuario)
        cursor.execute(consulta_cod_usu)
        rows = cursor.fetchall()
        connection.commit()
        cod_usu = rows[0][0]
        #nombre del archivo
        fecha_publi = datetime.datetime.now()
        consultaPreparada = 'INSERT INTO usuario (cod_usu, foto_publi, desc_publi, fecha_publi) VALUES ("{}", "{}", "{}", "{}");'.format(cod_usu,foto,descripcion,fecha_publi)
        cursor.execute(consulta_cod_usu)
        connection.commit()
        connection.close()

    def mostrarPublicacionPerfil(self):
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        preparada = 'Select * from publicacion where cod_usu = {}'.format(self.cod_usu)
        cursor.execute(preparada)
        rows = cursor.fetchall()
        connection.commit()
        return rows

    def mostrarPublicacionMain(self):
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        preparada = 'Select usuario.usuario, publicacion.cod_publi,publicacion.foto_publi,publicacion.desc_publi,publicacion.fecha_publi from usuario,publicacion where usuario.cod_usu = publicacion.cod_usu order by fecha_publi desc '
        cursor.execute(preparada)
        rows = cursor.fetchall()
        connection.commit()
        return rows

    def borrarPublicacion(self,cod_publi):
        preparada = 'DELETE FROM publicacion WHERE cod_publi="{}"'.format(cod_publi)
        connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
        cursor = connection.cursor()
        cursor.execute(preparada)
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        
    def mostrarPublicacionNOvista(self):
        preparada = "Select * from publicacion where "
        
    def editarPublicacion(self):
        pass