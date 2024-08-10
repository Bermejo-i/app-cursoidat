from util.conexiondb import Conexionbd

class cursodao:
    def __init__(self) -> None:
        self.conexion=Conexionbd().getConexionBD()

    def listarcursos(self):
        cursor=self.conexion.cursor()
        sql="select * from curso order by idcurso desc"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenercursos(self, idcurso):
        cursor=self.conexion.cursor()
        sql="select * from curso where idcurso='{}'".format(idcurso)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarcurso(self, curso ):
        exec =self.conexion.cursor()
        sql = "insert into curso values('{}','{}','{}')".format(curso.idcurso, curso.nomcurso, curso.credito)
        exec.execute(sql)
        self.conexion.commit()
        exec.close()
    
    def actualizarcurso(self, curso ):
        exec =self.conexion.cursor()
        sql = "update curso set nomcurso='{}', credito='{}' where idcurso='{}'".format(curso.nomcurso, curso.credito, curso.idcurso)
        exec.execute(sql)
        self.conexion.commit()
        exec.close()