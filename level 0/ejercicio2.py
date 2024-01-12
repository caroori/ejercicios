import sys
import os


monedaInicial = 0
monedaIntercambio = 0
opcion = 0
opMenu = 0


##info moneda
saldos = {
    'CLP': 500,
    'ARS': 60000,
    'USD': 800,
    'EUR': 90,
    'TRY': 0,
    'GBP': 0,

}

#monto mínimo y máximo para cada moneda, a elección
montoMinimo = {
    'CLP': 5,
    'ARS': 5,
    'USD': 5,
    'EUR': 5,
    'TRY': 5,
    'GBP': 5,
}

montoMaximo = {
    'CLP': 10000000,
    'ARS': 10000000,
    'USD': 10000000,
    'EUR': 10000000,
    'TRY': 10000000,
    'GBP': 10000000,
}


################################## F U N C I O N E S #################33###
##menu: El usuario puede decidir si retirar o no sus fondos. Si elige no retirar, debería regresar al menú principal.
def menu():
    print("1. Convertir moneda ")   
    print("2. Retirar fondos ")     # comisión del 1%.
    print("3. salir")

######## opcion 1 (((((convertir)))))
def convertidor(monedaInicial, monedaIntercambio, monto):
    global saldos
    #verifica el monto dentro de los limites
    if monto <= 0:
        print("El monto ingresado debe ser mayor que 0.")
    
    elif not (montoMinimo[monedaInicial] <= monto <= montoMaximo[monedaInicial]):   
       print("El monto ingresado no es correcto")
    
    # Verifica que la moneda inicial y la de intercambio existan
    elif monedaInicial not in saldos or monedaIntercambio not in saldos:
        print("Una o ambas monedas no existen.")
    
    else:       
        saldos[monedaInicial] -= monto
        saldos[monedaIntercambio] += monto
        
        #actualizacion de los saldos
        print(f"saldo en {monedaInicial}: {saldos[monedaInicial]}")
        print(f"saldo en {monedaIntercambio}: {saldos[monedaIntercambio]}")

######## opcion 2 (((((retirar fondos)))))
def retirar(moneda, monedaRetiro):
    global saldos
    saldoActual = saldos[moneda]  #busca el saldo que hay en la cuenta teniendo en cuenta esa moneda
    montoRetiro = min(max(0, saldoActual), saldoActual * 0.01)  ##el max es para asegurar que no sea negativo el saldoAct, el mín: asegura que hay un 1%
   
    # Verifica que el saldo actual sea mayor que 0
    if saldos[moneda] <= 0:
        print("El saldo actual debe ser mayor que 0")
    
    #verifica que el monto ingresado sea mayor que 0
    elif monedaRetiro <= 0:
        print("El monto de retiro debe ser mayor que 0")

    # Verifica que la moneda exista    
    elif moneda not in saldos: 
        print("La moneda no existe.")

    else:
        #calcula la comision
        comision = montoRetiro * 0.01
        montoRetiroTotal = montoRetiro + comision
        
        #verifica que el monto a retirar(con la comis) no sea mayor al saldo actual
        if montoRetiroTotal > saldos[moneda]:
            print("El monto a retirar excede el saldo actual")
            return
        
        saldos[moneda] -= montoRetiroTotal  ##se realiza la extracción 
        print(f"Retiro de {montoRetiro} en  {moneda}")
        print(f"Saldo actual en {moneda}: {saldos[moneda]}")



## consola
def limpiar_consola():
    sistema_operativo = os.name
    if sistema_operativo == 'posix':  # Linux y macOS
        os.system('clear')
    elif sistema_operativo == 'nt':   # Windows
        os.system('cls')
#### FIN FUNCIONES ###
        

#El usuario debe elegir su moneda inicial y la moneda a la que desea hacer el intercambio.

while opcion != 3: 
    menu()
    opMenu = int(input ("Ingrese una opcion: "))
    
    if opMenu == 1:
        limpiar_consola()
        print("1.CLP - 2.ARS - 3.USD - 4.EUR - 5.GBP")
        monedaInicial = input("Ingrese el nombre correspondiente a la moneda con la que desea operar: ").upper()   #upper es para hacer mayusculas en caso q se ingrese minusculas
        monedaIntercambio = input("Ingrese el nombre correspondiente a la moneda con la que desea hacer el intercambio: ").upper()
        monto = int(input("Ingrese el monto a convertir: "))
        convertidor(monedaInicial, monedaIntercambio, monto)
    
    elif opMenu == 2:
        limpiar_consola()
        print("1.CLP - 2.ARS - 3.USD - 4.EUR - 5.GBP")
        monedaRetiro = input("Ingrese el nombre correspondiente a la moneda con la que desea operar: ").upper()
        # Solicita al usuario el monto a retirar
        montoRetiro = int(input(f"Ingrese el monto a retirar en {monedaRetiro}: "))
        retirar(monedaRetiro, montoRetiro)
    
    elif opMenu == 3:
        limpiar_consola()
        print("Saliendo")
        sys.exit() 
    
    else:
        limpiar_consola()
        print("No existe esa opcion")