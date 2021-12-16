import cx_Oracle

class Nota():
    idNota=0
    nota1=0
    nota2=0
    nota3=0
    promedio=(nota1+nota2+nota3)/3
    idAlumno=""

    def __init__(self,idN,idA):
        self.idNota=idN
        self.idAlumno=idA

    def agregarNota():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            idAl=int(input("Indique Id de alumno: "))
            nota=int(input("Indique nota: "))
            cursor.execute(''' insert into notas (idNota, nota1,idAlumno) values (idNota.nextval, :no, :id) ''',no=nota,id=idAl)
            conexion.commit()
            print ("Nota agregada correctamente")
        except :
            print ("Oops! Intente nuevamente")
        
        finally:
            cursor.close()
            conexion.close()

    def editarNota1():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            idAl=int(input('Indique id de alumno: '))
            nota=int(input("Indique nueva nota: "))
            cursor.execute(''' update notas set nota1=:n1 where idAlumno=:id''',n1=nota,id=idAl)
            conexion.commit()
        except:
            print ("Error al editar, intente nuevamente!!")

        finally:
            cursor.close()
            conexion.close()

    def editarNota2():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            idAl=int(input('Indique id de alumno: '))
            nota=int(input("Indique nueva nota: "))
            cursor.execute(''' update notas set nota2=:n1 where idAlumno=:id''',n1=nota,id=idAl)
            conexion.commit()
        except:
            print("No fue posible editar Nota")

        finally:
            cursor.close()
            conexion.close()
    
    def editarNota3():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            idAl=int(input('Indique id de alumno: '))
            nota=int(input("Indique nueva nota: "))
            cursor.execute(''' update notas set nota3=:n1 where idAlumno=:id''',n1=nota,id=idAl)
            conexion.commit()
        except:
            print("No fue posible editar nota, intenten nuevamente!!")
        
        finally:
            cursor.close()
            conexion.close()

    def eliminarNota():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            idAl=int(input("Indique Id de alumno que desea eliminar: "))
            cursor.execute(''' delete into notas where idAlumno=:id ''',id=idAl)
            conexion.commit()
        except:
            print ("Error al eliminar nota, intente nuevamente!!")
        
        finally:
            cursor.close()
            conexion.close()

    def verNotasTodas():
        try:
            conexion=cx_Oracle.connect(
            user='escuela',
            password='1234',
            dsn='localhost:1521/xe')

            cursor=conexion.cursor()
            cursor.execute(''' select * from notas ''')
            resultado= cursor.fetchall()
            for row in resultado:
                print("|Codigo:",row[0],"|Nota 1:",row[1],"|Nota 2:",row[2],"|Nota 3:",row[3],"|Promedio:",row[4],"|Id Alumno:",row[5])
        
        except:
            print ("Error al mostrar notas, intente nuevamente!!")

        finally:
            cursor.close()
            conexion.close()

    def verNotasAlumno():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            nota= int(input("Indique Id de alumno a consultar: "))
            cursor.execute('''select * from notas where idAlumno=:cod''',cod=nota)
            resultado=cursor.fetchall()
            for row in resultado:
                print("|Codigo:",row[0],"|Notas:",row[1],"/",row[2],"/",row[3],"|Promedio:",row[4],"|Id Alumno:",row[5])

        except:
            print ("Error al mostrar notas alumno, intente nuevamente!!")

        finally:
            cursor.close()
            conexion.close()

    def seleccionaNotaEdit():
        seleccion=int(input("Indique nota que desea editar: "))
        if seleccion ==1:
            Nota.editarNota1()
        elif seleccion==2:
            Nota.editarNota2()
        elif seleccion==3:
            Nota.editarNota3()

    