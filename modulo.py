import cx_Oracle

class modulo():
    codigoSeccion=0
    ramo1=""
    ramo2=""
    ramo3=""
    ramo4=""

    def __init__(self,codSec) :
        self.codigoSeccion=codSec

    def crearModulo():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
                )
            cursor=conexion.cursor()
            codigoSeccion=input("Indique codigo de seccion a crear: ")
            ramo1=int(input("Indique ramo 1: "))
            ramo2=int(input("Indique ramo 2: "))
            ramo3=int(input("Indique ramo 3: "))
            ramo4=int(input("Indique ramo 4: "))
            cursor.execute(''' insert into secciones (codigosSeccion,ramo1,ramo2,ramo3,ramo4)
            values (:cs,:r1,:r2,:r3,:r4)''',cs=codigoSeccion,r1=ramo1,r2=ramo2,r3=ramo3,r4=ramo4)
            conexion.commit()
            print ("Seccion creada con exito!! ")
        except:
            print ("Error al crear modulo!!")
        
        finally:
            cursor.close()
            conexion.close()
   
    def editarModulo():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            codigoSeccion=input("Indique codigo de seccion a editar: ")
            ramo1=int(input("Indique nuevo ramo 1: "))
            ramo2=int(input("Indique nuevo ramo 2: "))
            ramo3=int(input("Indique nuevo ramo 3: "))
            ramo4=int(input("Indique nuevo ramo 4: "))
            cursor.execute('''  update secciones set ramo1=:r1, ramo2=:r2,ramo3=:r3,ramo4=:r4
            where codigosSeccion=:cod''',cod=codigoSeccion,r1=ramo1,r2=ramo2,r3=ramo3,r4=ramo4)
            conexion.commit()
            print ("Modulo editado correctamente!!")

        except:
            print ("Error al editar modulo!!")

        finally:
            cursor.close()
            conexion.close()
    
    def eliminarModulo():
        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            idS=input("Indique seccion que desea eliminar: ")
            cursor.execute(''' delete from secciones where codigosSeccion=:id ''',id=idS)
            conexion.commit()
            print ("Modulo eliminado correctamente!! ")
        except:
            print ("Error al eliminar modulo!!")

        finally:
            cursor.close()
            conexion.close()
    
    def mostrarModulos():

        try:
            conexion=cx_Oracle.connect(
                user='escuela',
                password='1234',
                dsn='localhost:1521/xe'
            )
            cursor=conexion.cursor()
            cursor.execute(''' select * from secciones ''')
            res=cursor.fetchall()
            for row in res:
                print("\n|Sección:",row[0], "|Ramos:", row[1],"-",row[2],"-",row[3],"-",row[4])
        
        except:
            print ("Error al mostrar modulos!! ")

        finally:
            cursor.close()
            conexion.close()