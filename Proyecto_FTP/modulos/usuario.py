from flask import Flask, render_template,request,redirect, url_for,flash
from flask_mysqldb import MySQL
import hashlib
import pymysql


app = Flask(__name__)


class UsuarioLog:
  
  def __init__(self, usuario,contrasena):
    
    self.usuario = usuario
    self.contrasena = contrasena

  def conectarUsuario(self):  
    cifrada = hashlib.md5((self.contrasena).encode('utf-8'))
    preparada = 'Select * from usuario where usuario = "{}" and contrasena = "{}";'.format(self.usuario,self.contrasena)
    #database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="redsocial")
    cursor = connection.cursor()
    cursor.execute(preparada)
    # some other statements  with the help of cursor

    rows = cursor.fetchall()
    for row in rows:
      print(row)

    connection.commit()
    connection.close()

    if len(rows) != 0:
      return True
    else: 
      return False