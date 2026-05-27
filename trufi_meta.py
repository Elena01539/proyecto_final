#este codigo te ayuda a ver que truffis de la ciudad de cercado pasan por los lugares turisticos de dicha ciudad
import time
usuario="Maria"
contraseña="mariaelena1"
cont=0
lista_destino={"cristo de la concordia":["linea 207","linea 230"],"la cancha":["trufi 101","micro 5","linea 12"],"plaza 14 de septiembre":["linea 109(panter rojo)","micro A","micro B"],"palacio portales":["linea 3","linea 5"],"parque de la familia":["linea 110","linea 7"],"laguna alalay":["linea 01","linea P","linea T"],"parque tunari":["trufis a chilimarca","trufis a tirani"],"jardin botanico martin cardenas":["linea 01","linea B","linea 244"],"teleferico":["linea 260","linea 2"],"museo convento santa teresa":["micro A","micro C","linea 110(San Martin)"]}

print("1.Registrarse ")
print("2.Iniciar sesion ")
print("3.Salir")
opcion=str(input("Elija una opcion: "))
if opcion=="1":
    lista=[]
    usuario=str(input("Usuario: "))
    contraseña=str(input("Contraseña: "))
    lista.append([usuario,contraseña])
    print("Bienvenid@ ",usuario)
    
    while True:
        destino=str(input("¿A que lugar turistico de cercado quiere ir? ")).strip().lower()
        if destino in lista_destino:
            print("Autos que pasan por ",destino)
            for auto in lista_destino[destino]:
                print("-",auto)
        else:
            print("Lugar no encontrado")
        print("1.Continuar")
        print("2.Salir ")
        opcion1=str(input("Elija una opcion: "))
        if opcion1=="2":
            print("Saliendo del sistema..")
            break
        elif opcion1 !="1":
            print("Opcion invalida,continuando por defecto")
if opcion=="2":
    while cont<=3:
        usuario1=str(input("Ingrese su nombre de usuario: "))
        contraseña1=str(input("Ingrese su contraseña: "))
        if contraseña1==contraseña and usuario1==usuario:
            print("Bienvenido")
            break
        if contraseña1!=contraseña or usuario1!=usuario:
            print("Contraseña o usuario incorrecto,intente de nuevo:")
            cont=cont+1
            if cont>3:
                print("demasiados intentos espere un momento antes de intentar de nuevo")
                time.sleep(5)
                cont=0
    while True:
        destino=str(input("¿A que lugar turistico de cercado quiere ir? ")).strip().lower()
        if destino in lista_destino:
            print("Autos que pasan por ",destino)
            for auto in lista_destino[destino]:
                print("-",auto)
        else:
            print("Lugar no encontrado")
        print("1.Continuar")
        print("2.Salir ")
        opcion1=str(input("Elija una opcion: "))
        if opcion1=="2":
            print("Saliendo del sistema..")
            break
        elif opcion1 !="1":
            print("Opcion invalida,continuando por defecto")

if opcion=="3":
    print("Vuelva pronto ")


