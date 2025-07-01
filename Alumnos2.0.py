alumno1={ "rut":"11111111-1",
          "nombre":"Alexis Sánchez",
          "edad":36
        }
alumno2={ "rut":"22222222-2",
          "nombre":"Shakira",
          "edad":50
        }
alumno3={ "rut":"3333333-3",
          "nombre":"Donald Trompeta",
          "edad":65
        }
alumnos=[alumno1,alumno2,alumno3]
while True:
    print('Menú de Opciones')
    print('1.- Agregar Alumno')
    print('2.- Mostrar Alumnos')
    print('3.- Mostrar Alumnos por Rango de Edad')
    print('S.- Salir')
    opcion=input('Ingrese Opcio: ')
    if opcion=='1':
        print('Agregar')
    elif opcion=='2':
        for alumno in alumnos:
                print(alumno)
    elif opcion=='3':
        print('Mostrar por Rango')
    elif opcion.upper()=='S':
        print('Gracias por Preferirnos')
        break
    else:
        print('Opcion Incorrecta')
'''
rut="xxx"
while rut!="-1":
    rut=input('Ingrese rut: ')
    nombre=input('Ingrese Nombre: ')
    edad=int(input('Ingrese Edad: '))
    alumno={}
    alumno["rut"]=rut   
    alumno["nombre"]=nombre 
    alumno["edad"]=edad
    alumnos.append(alumno)  
for alumno in alumnos:
    print(alumno)


for alumno in alumnos:
    for clave,valor in alumno.items():
        print(alumno)
        if clave=="edad" and valor>=50:
            print(alumno["nombre"],alumno.get("nombre1",0))
        print(alumno)
'''