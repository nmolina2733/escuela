  

from alumno import alumno
from matricula import matricula
from modulo import modulo
from nota import Nota


def menuProfesor():
    salir=True
    while (salir):
        noSalir=False
        while (not noSalir):
            print ("==================================================")
            print ("|=============== Menu Profesor  =================|")
            print ("| 1) Ver Alumnos seccion                         |")
            print ("| 2) Editar Notas Alumnos                        |")
            print ("| 3) Ver Notas Alumnos                           |")
            print ("| 4) Eliminar notas alumno                       |")
            print ("| 5) Agregar nota alumno                         |")
            print ("| 5) Volver                                      |")
            print ("| 6) Salir                                       |")
            print ("==================================================")
            opcion = int(input("Indique selección: "))
            if opcion <1 or opcion >6:
                print ("La opción ingresada no es valida, intente nuevamente!!")
            elif opcion ==1:
                alumno.verTodosAlumnos()
            elif opcion ==2:
                Nota.seleccionaNotaEdit()
            elif opcion ==3:
                Nota.verNotasAlumno()
            elif opcion ==4:
                Nota.eliminarNota()
            elif opcion ==5:
                Nota.agregarNota()
            elif opcion ==5:
                menuIngreso()
            elif opcion ==6:
                print ("Gracias por usar mi programa!!")
                exit()
            
            else:
                print ("La opcion ingresada no es valida!! ")

def menuAdministrador():
    salir=True
    while (salir):
        noSalir=False
        while (not noSalir):
            print ("==================================================")
            print ("|============ Menu Administrador =================")
            print ("| 1) Matricular                                  |")
            print ("| 2) Editar Matricula                            |")
            print ("| 3) Ver alumnos matriculados                    |")
            print ("| 4) Eliminar matricula                          |")
            print ("| 5) Volver                                      |")
            print ("| 6) Salir                                       |")
            print ("==================================================")
            opcion = int(input("Indique selección: "))
            if opcion <1 or opcion >6:
                print ("La opción ingresada no es valida, intente nuevamente!!")
            elif opcion ==1:
                matricula.matricular()
            elif opcion ==2:
                matricula.editarMatricula()
            elif opcion ==3:
                matricula.listarMatriculados()
            elif opcion ==4:
                matricula.eliminarMatricula()
            elif opcion==5:
                menuIngreso()
            elif opcion ==6:
                print ("Gracias por usar mi programa!!")
                exit()
            
            else:
                print ("La opcion ingresada no es valida!! ")

    

def menuAlumno():
    salir=True
    while (salir):
        noSalir=False
        while (not noSalir):
            print ("==================================================")
            print ("|=============== Menu Alumno  ===================|")
            print ("| 1) Ver Notas                                   |")
            print ("| 2) ver Seccion                                 |")
            print ("| 3) Ver Cuotas por pagar                        |")
            print ("| 4) Ver Profesor por sección                    |")
            print ("| 5) Volver                                      |")
            print ("| 6) Salir                                       |")
            print ("==================================================")
            opcion = int(input("Indique selección: "))
            if opcion <1 or opcion >6:
                print ("La opción ingresada no es valida, intente nuevamente!!")
            elif opcion ==1:
                Nota.verNotasAlumno()
            elif opcion ==2:
                pass  #falta mostrar modulo solo alumno
            elif opcion ==3:
                pass 
            elif opcion ==4:
                pass
            elif opcion ==5:
                menuIngreso()
            elif opcion ==6:
                print ("Gracias por usar mi programa!!")
                exit()
            
            else:
                print ("La opcion ingresada no es valida!! ")



def menuIngreso():
    salir=True
    while (salir):
        noSalir=False
        while (not noSalir):
            print ("==================================================")
            print ("|============= Menu Ingreso =====================|")
            print ("| 1) Menu Alumno                                 |")
            print ("| 2) Menu Profesor                               |")
            print ("| 3) Menu Administrador                          |")
            print ("| 4) Cambiar contraseña                          |")
            print ("| 5) Salir                                       |")
            print ("==================================================")
            opcion= int (input("Ingrese selección: "))
            if opcion <1 or opcion >5:
                print ("La opción ingresada no es valida, intente nuevamente!!")
            elif opcion ==1:
                menuAlumno()
            elif opcion ==2:
                menuProfesor()
            elif opcion ==3:
                menuAdministrador()
            elif opcion ==4:
                pass
            elif opcion ==5:
                print ("Gracias por usar mi programa!!")
                exit()
            else:
                print ("La opcion ingresada no es valida!! ")

