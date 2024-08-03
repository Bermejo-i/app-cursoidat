from util.conexiondb import Conexionbd

class cursodao:
    def __init__(self) -> None:
        self.conexion=Conexionbd().getConexionBD()

    def listarcursos(self):
        cursor=self.conexion.cursor()
        sql="select * from curso order by idcurso desc"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def insertarcurso(self, curso ):
        exec =self.conexion.cursor()
        sql = "insert into curso values('{}','{}','{}')".format(curso.codcurso, curso.nomcurso, curso.credcurso)
        exec.execute(sql)
        self.conexion.commit()
        exec.close()
    