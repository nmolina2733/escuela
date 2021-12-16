import cx_Oracle

class matricula():
    codigoMatricula=0
    rut=""
    carrera=""
    fecha=""
    semestre=""
    valorMatricula=0
    cuotas=0
    metodoPago=""

    def __init__(self,codM,rt,ca,fe,sem,valMa,cu,mp):
        self.codigoMatricula=codM
        self.rut=rt
        self.carrera=ca
        self.fecha=fe
        self.semestre=sem
        self.valorMatricula=valMa
        self.cuotas=cu
        self.metodoPago=mp

    def matricular():
        try:
            conexion= cx_Oracle.connect(
                    user = 'escuela',
                    password = '1234',
                    dsn = 'localhost:1521/xe')
            cursor=conexion.cursor()
            rut=input("Ingrese RUT de alumno\n")
            carrera=int(input("Indique carrera alumno\n | 1) Programacion |\n | 2) Administracion | \n | 3) Mecanica | \n | 4) Diseño | \n | 5) Cocina internacional |\n"))
            fecha=input("Indique fecha de matricula\n")
            semestre=input("Indique semestre a matricular\n")
            valorMatricula=int(input("Indique valor de matricula\n"))
            cuotas=int(input("Indique cantidad de cuotas\n"))
            metodoPago=input("Indique modalidad de pago\n")
            cursor.execute('''insert into matriculas (codigoMatricula,rut,carrera,fecha,semestre,valorMarticula,cuotas,metodoPago)
            values (codigoMatricula.nextval,:rt,:ca,:fe,:se,:val,:co,:met) ''',rt=rut,
            ca=carrera,fe=fecha,se=semestre,val=valorMatricula,co=cuotas,met=metodoPago)
            conexion.commit()
            print ("Matriculado correctamente")
        
        except:
            print ("Error al matricular, intente nuevamente!!")

        finally:
            cursor.close()
            conexion.close()

    def eliminarMatricula():
        try:
            conexion= cx_Oracle.connect(
                    user = 'escuela',
                    password = '1234',
                    dsn = 'localhost:1521/xe')
            cursor=conexion.cursor()
            codigoMatricula= int(input("Indique codigo de matricula\n"))
            cursor.execute(''' delete from matriculas where codigoMatricula=:codMa ''',codMa=codigoMatricula)
            conexion.commit()
            print ("Alumno eliminado correctamente")
        except:
            print ("Error al eliminar matricula de alumno!!")
        
        finally:
            cursor.close()
            conexion.close()

    def listarMatriculados():

        try:
            conexion= cx_Oracle.connect(
                    user = 'escuela',
                    password = '1234',
                    dsn = 'localhost:1521/xe')
            cursor=conexion.cursor()
            cursor.execute(''' select * from matriculas ''')
            resultado=cursor.fetchall()
            for row in resultado:
                print("\n|Codigo",row[0], "|Rut",row[1],"|Carrera",[2], "|Fecha",row[3],"|Semestre",row[4],"|Valor Matricula",row[5],"|Cuotas",row[6],"|MetodoPago",row[7] )
        except:
            print ("Error al mostrar matriculas!! ")

        finally:
            cursor.close()
            conexion.close()

    def editarMatricula():
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
            print ("Error al editar matricula alumno!!")
        
        finally:
            cursor.close()
            conexion.close()
