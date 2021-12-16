import cx_Oracle

class alumno():
    codigoAlumno=0
    nombre=""
    carrera=""
    modulo=""
    jornada=""

    def __init__(self,cod,nom,car,mod,jor):
        self.codigoAlumno=cod
        self.nombre=nom
        self.carrera=car
        self.modulo=mod
        self.jornada=jor

    def agregarAlumnos():
        try:
            conexion= cx_Oracle.connect(
                    user = 'escuela',
                    password = '1234',
                    dsn = 'localhost:1521/xe')
            cursor=conexion.cursor()
            nombre=input("Ingrese nombre\n")
            carrera=input("Ingrese carrera\n")
            modulo=input("Indique modulo\n")
            jornada=input("Indique jornada\n")
            cursor.execute('''insert into alumnos (codigoAlumno,nombre,carrera,modulo,jornada)
            values (codigoAlumno.nextval,:no, :ca,:mo,:jo) ''',no=nombre,
            ca=carrera,mo=modulo,jo=jornada)
            conexion.commit()
        except:
            print ("Error al ingresar nuevo alumno, intente nuevamente!! ")

        finally:
            cursor.close()
            conexion.close()

    def editarModuloAlumno():
        try:
            conexion= cx_Oracle.connect(
                    user = 'escuela',
                    password = '1234',
                    dsn = 'localhost:1521/xe')
            cursor=conexion.cursor()
            codAl= int (input("Indique codigo alumno: "))
            nuevoM = input("Indique nueva seccion: ")
            cursor.execute('''update alumnos set modulo=:nv where codigoAlumno=:ca ''',nv=nuevoM,ca=codAl)
            conexion.commit()
        except:
            print ("Error al editar Modulo!!")
        
        finally:
            cursor.close()
            conexion.close()

    def verTodosAlumnos():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn= 'localhost:1521/xe'
            )
            cursor=conexion.cursor()
            cursor.execute('''select * from alumnos''')
            resultado=cursor.fetchall()
            for row in resultado:
                print("\n|Cod:",row[0],"|Nombre:",row[1],"|Carrera:",row[2],"|Modulo:",row[3],"|Jornada:",row[4],"|")

        except:
            print ("Error al mostrar alumnos")

        finally:
            cursor.close()
            conexion.close()

    def verAlumno():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            codigo=int(input("Indique el codigo de alumno a consultar: "))
            cursor.execute('''select codigoAlumno,nombre,carrera from alumnos where codigoAlumno=:cod''',cod=codigo)
            resultado=cursor.fetchmany(3)
            for row in resultado:
                print("|Codigo:",row[0],"|Nombre:",row[1],"|Carrera:",row[2])
        except:
            print ("Error al ver alumno")
        
        finally:
            cursor.close()
            conexion.close()


    
    