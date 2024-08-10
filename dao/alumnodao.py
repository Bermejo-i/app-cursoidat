from util.conexiondb import Conexionbd

class alumnodao:
    def __init__(self) -> None:
        self.conexion=Conexionbd().getConexionBD()

    def listaralumnos(self):
        cursor=self.conexion.cursor()
        sql="select a.idalumno, a.nomalumno, a.apealumno, e.nomesp from alumno a INNER JOIN especialidad e ON a.IdEsp=e.IdEsp"
        +"order by a.idalumno desc"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obteneralumnos(self, idalumno):
        cursor=self.conexion.cursor()
        sql = "select a.idalumno, a.nomalumno, a.apealumno, e.nomesp, a.proce from alumno a INNER JOIN especialidad e ON a.IdEsp=e.IdEsp"
        sql += "where a.idalumno='{}'".format(idalumno)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertaralumno(self, alumno ):
        exec =self.conexion.cursor()
        sql = "insert into alumno values('{}','{}','{}','{}','{}')".format(alumno.codalumno, alumno.nomalumno, alumno.apealumno, 
                                                                           alumno.idespecialidad, alumno.procedencia)
        exec.execute(sql)
        self.conexion.commit()
        exec.close()
    
    def actualizaralumno(self, alumno ):
        exec =self.conexion.cursor()
        sql = "update alumno set nomalumno='{}', apalumno='{}',idesp='{}', proce='{}' where"
        sql += " idalumno='{}'".format(alumno.nomalumno, alumno.apealumno, alumno.idesp, alumno.proce, alumno.idalumno)
        exec.execute(sql)
        self.conexion.commit()
        exec.close() 