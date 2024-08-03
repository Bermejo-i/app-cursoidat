from util.conexiondb import Conexionbd

class alumnodao:
    def __init__(self) -> None:
        self.conexion=Conexionbd().getConexionBD()

    def listaralumnos(self):
        cursor=self.conexion.cursor()
        sql="select * from alumno order by idalumno desc"
        cursor.execute(sql)
        return cursor.fetchall()