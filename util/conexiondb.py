import mysql.connector

class Conexionbd:
    def __init__(self,):
        self.conexion=mysql.connector.connect(host='localhost', database='bdnotas' ,user='root' ,password='123456')

    def getConexionBD(self):
        return self.conexion