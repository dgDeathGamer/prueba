from Tv import Tv
from consola import Consola
from Scooter import Scooter
from Bicicleta import Bicicleta 

listaTVs = []
listaConsolas = []
listaScooters = []
listaBicicletas = []

def registrarTv():
    marca = input("Ingrese la marca del TV: ")
    voltaje = int(input("Ingrese el voltaje del TV: "))
    precio = float(input("Ingrese el precio del TV: "))
    eficiencia = input("Ingrese la eficiencia del TV (A, B, C, D o E): ")
    tamaño = float(input("Ingrese el tamaño del TV en pulgadas: "))

    tv = Tv(marca, voltaje, precio, eficiencia, tamaño)
    listaTVs.append(tv) #append para cargar lo que esta en listaTVs[] 

def registrarConsola():
    nombreConsola = input("Ingrese el nombre de la Consola: ")
    version = input("Ingrese la versión de la Consola: ")
    marca = input("Ingrese la marca de la Consola: ")
    voltaje = int(input("Ingrese el voltaje de la Consola: "))
    precio = float(input("Ingrese el precio de la Consola: "))
    eficiencia = input("Ingrese la eficiencia de la Consola (A, B, C, D o E): ")

    consola = Consola(nombreConsola, version, marca, voltaje, precio, eficiencia)
    listaConsolas.append(consola)

def registrarScooter():
    marca = input("Ingrese la marca del Scooter: ")
    voltaje = int(input("Ingrese el voltaje del Scooter: "))
    precio = float(input("Ingrese el precio del Scooter: "))
    eficiencia = input("Ingrese la eficiencia del Scooter (A, B, C, D o E): ")
    aro = float(input("Ingrese el aro del Scooter: "))
    velocidad = int(input("Ingrese la velocidad máxima del Scooter en km/h: "))
    peso = float(input("Ingrese el peso del Scooter en kg: "))

    scooter = Scooter(marca, voltaje, precio, eficiencia, aro, velocidad, peso)
    listaScooters.append(scooter)

def registrarBicicleta():
    marca = input("Ingrese la marca de la Bicicleta: ")
    voltaje = int(input("Ingrese el voltaje de la Bicicleta: "))
    precio = float(input("Ingrese el precio de la Bicicleta: "))
    eficiencia = input("Ingrese la eficiencia de la Bicicleta (A, B, C, D o E): ")
    aro = float(input("Ingrese el aro de la Bicicleta: "))
    peso = float(input("Ingrese el peso de la Bicicleta en kg: "))

    bicicleta = Bicicleta(marca, voltaje, precio, eficiencia, aro, peso)
    listaBicicletas.append(bicicleta)

def cotizarTvs():
    for tv in listaTVs:
        tv.cotizar()
        print(tv)

def cotizarConsolas():
    for consola in listaConsolas:
        consola.cotizar()
        print(consola)

def cotizarScooters():
    for scooter in listaScooters:
        scooter.cotizar()
        print(scooter)

def cotizarBicicletas():
    for bicicleta in listaBicicletas:
        bicicleta.cotizar()
        print(bicicleta)

def menu():
    opcion = ""
    while opcion != '9':
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar TVs")
        print("6. Cotizar Consolas")
        print("7. Cotizar Scooters")
        print("8. Cotizar Bicicletas")
        print("9. Salir")

        opcion = input("Ingrese una opción del 1 al 9: ")

        if opcion == "1":
            registrarTv()
        elif opcion == "2":
            registrarConsola()
        elif opcion == "3":
            registrarScooter()
        elif opcion == "4":
            registrarBicicleta()
        elif opcion == "5":
            cotizarTvs()
        elif opcion == "6":
            cotizarConsolas()
        elif opcion == "7":
            cotizarScooters()
        elif opcion == "8":
            cotizarBicicletas()
        elif opcion == "9":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()