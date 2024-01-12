#Crear un sistema de envío en línea con las siguientes características:
#El sistema tiene un inicio de sesión que se bloquea después del tercer intento fallido.
#Mostrar un menú que permite: Enviar un paquete, salir del sistema.
#Para enviar un paquete, se requieren detalles del remitente y del destinatario.
#El sistema asigna un número de paquete aleatorio a cada paquete enviado.
#El sistema calcula el precio del envío. $2 por kg.
#El usuario debe ingresar el peso total de su paquete y el sistema debería mostrar la cantidad a pagar.
#El sistema debe preguntar si el usuario desea realizar otra operación. Si la respuesta es sí, debería volver al menú principal. Si es no, debería cerrar el sistema.

import time
import sys
import os
import random


user_ = "admin"
pwd_ = "123"

contador = 0
opcion = 0

##################################     F U N C I O N E S            ######################

def menu():
    print("1. Enviar paquete")
    print("2. Salir")

def envios():
    #### datos 
    remitente = input("Ingrese su apellido: ")
    destinatario = input("Ingrese el apellido del destinatario: ")
    peso = float(input("Ingrese el peso del paquete (kg): "))
    
    ##general
    limpiar_consola()
    numeroPaquete = random.randint(1000, 9999)
    precioEnvio = peso * 2
    print(f"El costo del envio es de: {precioEnvio}")
    print(f"Detalles del remitente: {remitente}")
    print(f"Detalles del destinatario: {destinatario}")
    print(f"Numero de envio: {numeroPaquete}")

def subMenu():
    continuar = input("¿Desea realizar otra operacion? (SI/NO): ").lower()   #lower para que sea minisculas en caso q se ingrese mayusc
    if continuar == 'si':
        limpiar_consola()
        return True
    elif continuar == 'no':
        print("Saliendo")
        sys.exit()
    else:
        print("Respuesta no válida")
        print("")
        return subMenu()


#### CONSOLA
def limpiar_consola():
    sistema_operativo = os.name
    if sistema_operativo == 'posix':  # Linux y macOS
        os.system('clear')
    elif sistema_operativo == 'nt':   # Windows
        os.system('cls')

##################################     F I N - - F U N C I O N E S  ######################


while (contador < 3):              #mientras que el contador no sea superior a 3, puede seguir intentando ingresar
    user = input("Usuario: ")                 #carga los datos ingresados
    pwd = input("Contraseña: ")               #carga los datos ingresados
    
    if user == user_ and pwd == pwd_:   #verifica que coincida (si hay coincidencia)
        limpiar_consola()
        print("Bienvenido al sistema de envios")             #caso correcto (ingreso)
        print(" ")
        ###### MENU
        while True:
            menu()
            opcion = int(input ("Ingrese una opcion: "))

            ##caso selección
            if opcion == 1:          
                limpiar_consola()
                envios()

            elif opcion == 2:
                limpiar_consola()
                print("Saliendo del sistema, espere...")
                time.sleep(2)
                limpiar_consola()
                break
            else:
                print("no existe esa opcion")
            contador += 1

            ##### pregunta si se desea realizar otra operación
            if not subMenu():   ##para salir
                break
            else:               ##en caso que sí desee, continua con el bucle
                limpiar_consola()

    
    else:                   #si no coincide 
        limpiar_consola()
        print ("usuario o contraseña incorrecto, vuelva a ingresar los datos...")       #caso incorrecto
        time.sleep(1)
        limpiar_consola()
        if contador == 2:                           #en el caso que sea 3 los intentos hechos, bloquea la cuenta
            limpiar_consola()
            print("acceso bloqueado")
            break
        contador += 1 

    

