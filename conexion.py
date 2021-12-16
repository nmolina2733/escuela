import cx_Oracle
class conexion():

    def __init__(self):
        try:
            conexion= cx_Oracle.connect(
                user = 'escuela',
                password = '1234',
                dsn = 'localhost:1521/xe')
                
        except:
            print ("No fue posible conectar")

        finally:
            conexion.close()
    
    def mostrar():
        conexion= cx_Oracle.connect(
                user = 'escuela',
                password = '1234',
                dsn = 'localhost:1521/xe')
        cursor=conexion.cursor()
        cursor.execute('''select * from alumnos''')
        resultado = cursor.fetchall()
        print (resultado)

    def editar():
        conexion= cx_Oracle.connect(
                user = 'escuela',
                password = '1234',
                dsn = 'localhost:1521/xe')
        cursor=conexion.cursor()
        codAl= int (input("Indique codigo alumno: "))
        nuevoM = input("Indique nueva seccion: ")
        cursor.execute('''update alumnos set modulo=:nv where codigoAlumno=:ca ''',nv=nuevoM,ca=codAl)
        conexion.commit()
    
    def agregar():
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
    
    def eliminar():
        conexion= cx_Oracle.connect(
                user = 'escuela',
                password = '1234',
                dsn = 'localhost:1521/xe')
        cursor=conexion.cursor()
        nombre=input("Indique alumno que desea eliminar\n")
        cursor.execute(''' delete from alumnos where nombre=:no''', no=nombre)
        conexion.commit()
