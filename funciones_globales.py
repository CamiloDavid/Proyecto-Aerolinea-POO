

# importo datetime para las fechas
from datetime import datetime as fecha

# _____________________________________________________________________________________

# Definimos la constante para el formato de fecha al inicio del archivo
FECHA_FORMAT = "%Y-%m-%d %H:%M:%S"
FECHA_FORMAT_2 = "%d-%m-%Y"

# Métodos globales

# función para que validar que la fecha tenga el formato correcto, y no haya ingresado una fecha incorrecta, retorna el objeto tipo datetime
def ingresar_fecha_nacimiento_valida():

    # la única forma que rompa el bucle es que la fecha tenga un formato correcto, y una fecha pasada
    while True:
        fecha_nacimiento = input('Dime tu fecha de nacimiento con el siguiente formato (dd-mm-yyyy): ')
        try:
            #convertir la cadena a un objeto de fecha con el formato dado
            fecha_valida = fecha.strptime(fecha_nacimiento, FECHA_FORMAT_2).date()

            # Obtener la fecha actual sin la hora
            fecha_actual = fecha.now().date()

            # Comprobar si la fecha ingresada es mayor que la fecha actual
            if fecha_valida > fecha_actual:
                print(f'Error, la fecha: {fecha_nacimiento} es una fecha futura')
            else: 
                return fecha_valida # retorno la fecha
            
        except ValueError as e:
            # Si ocurre un ValueError, la fecha no es válida
            print(f'Error, la fecha: {fecha_nacimiento}, no tiene el formato correcto o es una fecha inválida')

# _____________________________________________________________________________________

# función para validar que el usuario haya ingresado una cedula numérica entera y sea positiva
def ingresar_cedula_valida():
    while True:
        try:
            cedula = int(input('\nDime el número de la cédula, solo números, sin puntos: '))
            # valido que la cedula sea un número positivo
            if cedula > 0: #
                return cedula
            else:
                print(f'la cedula ingresada: {cedula}, debe ser positiva, vuelve a intentarlo')
                
        except ValueError as e:
            print(f'error: {e}, vuelve a intentarlo')

# _____________________________________________________________________________________

# función que calcula la edad de una persona
def calcular_edad(fecha_nacimiento):

    # consigo la fecha
    fecha_actual = fecha.now().date()
    
    # bloque para calcular la edad
    edad = fecha_actual.year - fecha_nacimiento.year

    # Ajusto si la persona no ha cumplido años este año
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return edad


# _____________________________________________________________________________________

# función para convertir de tipo str a datetime, formato: "%Y-%m-%d %H:%M:%S"
def convertir_str_a_datetime(cadena_fecha_hora):
    
    # Convertir la cadena a un objeto datetime usando strptime
    fecha_hora = fecha.strptime(cadena_fecha_hora, FECHA_FORMAT)
    
    return fecha_hora

# _____________________________________________________________________________________

def solicitar_nuevos_datos() -> dict:

    print('---------- Nuevos Datos ------------')
    
    id = ingresar_cedula_valida()
    fecha_nacimiento = ingresar_fecha_nacimiento_valida()
    edad = calcular_edad(fecha_nacimiento)
    nombres = input('\nDime los nombres: ')
    apellidos = input('Dime los apellidos: ')

    nuevos_atributos = {
        'id': id,
        'fecha_nacimiento': fecha_nacimiento,
        'edad': edad,
        'nombres':nombres,
        'apellidos': apellidos
    }

    return nuevos_atributos

# _____________________________________________________________________________________

def elegir_clase_tiquete():

    while True:
        print('''
        ------ Clases de Tiquete -----
        1. Clase Baja: 150000 pesos
        2. Clase ALta: 300000 pesos
        ------------------------------
        ''')

        try:
            opc = int(input('Ingresa una opción (1 o 2): '))
            if opc == 1:
                return 'Baja'
            elif opc == 2:
                return 'Alta'
            else:
                print('Ingresaste un valor distinto de 1 o 2')
        except ValueError as e:
            print(f'error: {e}, ingresaste un valor no entero, vuelve a intentarlo')

# _____________________________________________________________________________________

# función para elegir el destino
def elegir_destino_vuelo() -> str:

    destino = None

    while True:
        print('''
        ------ Destinos de Vuelo -----
        1. Bogotá
        2. Cali
        3. Medellin
        4. Pereira
        5. Cartagena
        ------------------------------
        ''')

        try:
            opc = int(input('Ingresa una opción (1-5): '))
            if opc == 1:
                destino = 'Bogota'
            elif opc == 2:
                destino = 'Cali'
            elif opc == 3:
                destino = 'Medellin'
            elif opc == 4:
                destino = 'Pereira'
            elif opc == 5:
                destino = 'Cartagena'
            else:
                print('Ingresaste una opción inválida, vuelve a intentarlo')
        except ValueError as e:
            print(f'error: {e}, ingresaste un valor no entero, vuelve a intentarlo')

        if destino != None:
            return destino

# _____________________________________________________________________________________

def asignar_precio_vuelo(clase) -> int:

    # si eligio la clase baja
    if clase == 'Baja':
        # asigno el precio correspondiente
        precio = 150000
    # si eligio la clase alta
    elif clase == 'Alta':
        precio = 300000
    else:
        precio = 150000
        
    return precio

# _____________________________________________________________________________________

# el argumento que recibe es un objeto tipo Date
def elegir_fecha_vuelo(fecha_compra_tiquete):

    # la única forma que rompa el bucle es que la fecha tenga un formato correcto, y una fecha posterior al de la compra
    while True:
        fecha_vuelo = input('Dime la fecha del vuelo con el siguiente formato (dia-mes-año): ')
        try:
            #convertir la cadena a un objeto de fecha con el formato dado
            fecha_valida = fecha.strptime(fecha_vuelo, FECHA_FORMAT_2)

            # Comprobar si la fecha ingresada es mayor que la fecha de la compra del tiquete
            if fecha_valida.date() > fecha_compra_tiquete:
                return fecha_vuelo # retorno la fecha
            else: 
                print(f'Error, la fecha: {fecha_vuelo} es una fecha igual o anterior a la fecha de la compra del tiquete')
            
        except ValueError as e:
            # Si ocurre un ValueError, la fecha no es válida
            print(f'Error, la fecha: {fecha_vuelo}, no tiene el formato correcto o es una fecha inválida')
