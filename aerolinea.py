
# importo datetime para las fechas
from datetime import datetime as fecha
from usuario import Usuario
from vuelo import Vuelo
import archivo_texto

# _____________________________________________________________________________________

# Definimos la constante para el formato de fecha al inicio del archivo
FECHA_FORMAT = "%Y-%m-%d %H:%M:%S"

# _____________________________________________________________________________________

class Aerolinea:

    # método constructor
    def __init__(self) -> None:
        self.__usuarios = []

# _____________________________________________________________________________________

    # métodos get
    @property
    def usuarios(self):
        return self.__usuarios

# _____________________________________________________________________________________

    # el siguiente método solo se encarga de crear un objeto usuario, con la validación de que sea mayor de 18, y 
    # la cédula no se repita con la de un usuario en la lista de usuarios
    def crear_usuario(self) -> Usuario:

        print('\n------Usuario a Crear -------')
        id = ingresar_cedula_valida()
        usuario = self.buscar_usuario(id)

        if usuario == None:
            fecha_nacimiento = ingresar_fecha_nacimiento_valida()
            edad = calcular_edad(fecha_nacimiento)
            if edad >= 18:
                nombres = input('\nDime los nombres: ')
                apellidos = input('Dime los apellidos: ')
            else:
                print(f'\nTu edad es: {edad}, debes ser mayor de edad')
                return None
        else:
            print(f'\nUsuario con cédula: {id}, ya está registrado: \n{usuario}')
            return None
        
        # creo objeto
        usuario = Usuario(id,nombres, apellidos, fecha_nacimiento, edad)
        return usuario
# _____________________________________________________________________________________
    # métodos de instancia

    # función buscar_usuario, lo busca por la cédula si lo encuentra retorna el objeto usuario, sino None
    def buscar_usuario(self, cedula) -> Usuario:
        # voy a recorrer la lista de usuarios, cada usuario es un objeto
        for usuario in self.usuarios:
            # si los números de la cédula coinciden
            if usuario.id == cedula:
                return usuario # retorno el objeto usuario
        # Al salir del bucle quizo decir que no encontró el usuario
        return None

# _____________________________________________________________________________________

    # función posicion_usuario, lo busca por la cédula si lo encuentra retorna la posición en la lista
    def encontrar_posicion_usuario(self, cedula):
        # voy a recorrer la lista de usuarios, cada usuario es un objeto
        for i, usuario in enumerate(self.usuarios):
            # si los números de la cédula coinciden
            if usuario.id == cedula:
                return i # retorno el objeto usuario
        # Al salir del bucle quizo decir que no encontró el usuario
        return -1

# _____________________________________________________________________________________

    # función para consultar un usuario
    def mostrar_usuario(self):

        print('\n-------- Usuario a Buscar---------')
        cedula = ingresar_cedula_valida()
        usuario = self.buscar_usuario(cedula)
        if usuario != None:
            print(f'\nUsuario encontrado: {usuario}')
        else:
            print(f'\nEl usuario con cédula: {cedula}, no está registrado')

# _____________________________________________________________________________________

    # función para mostrar usuarios
    def mostrar_usuarios(self):

        print('\n----------- Usuarios registrados -----------')
        for i, usuario in enumerate(self.usuarios):
            print(f'Usuario # {i+1}: {usuario}' )

# _____________________________________________________________________________________

    # añade el usuario en la lista usuarios
    def registrar_usuario(self):

        print('\n------Proceso de Registro -------')

        usuario = self.crear_usuario()

        # verifico que el usuario si se pudo crear
        if usuario != None: 

            # añado el usuario en la lista de usuarios
            self.usuarios.append(usuario)

            # obtengo la fecha actual, año, mes, dia, hora, minuto, segundo, y la convierto a tipo datetime
            fecha_actual = convertir_str_a_datetime(fecha.now().strftime(FECHA_FORMAT))

            # función para adicionar información fichero reglog.txt, le paso la fecha actual
            archivo_texto.adicionar_info_reglog(usuario, fecha_actual)

            # confirmo que el usuario se registró
            print(f'''
                el usuario se ha registrado exitosamente:
                {usuario}
            ''')

# _____________________________________________________________________________________

    def actualizar_usuario(self):

        # muestro los usuarios que están registrados hasta el momento
        self.mostrar_usuarios()
            
        print('\nIngrese la cédula con que aparece registrado: ')
        cedula_antigua = ingresar_cedula_valida()
        pos = self.encontrar_posicion_usuario(cedula_antigua)

        print(f'\nUsuario a actualizar: {self.usuarios[pos]}')
        
        # obtengo los nuevos datos y los almaceno en un diccionario
        nuevos_datos = solicitar_nuevos_datos()

        if nuevos_datos.get('edad') >= 18: # si es mayor de edad
            
            # actualizo los atributos
            for atributo, valor in nuevos_datos.items():
                setattr(self.usuarios[pos], atributo, valor)

            # obtengo la fecha actual, año, mes, dia, hora, minuto, segundo, y la convierto a tipo datetime
            fecha_actual = convertir_str_a_datetime(fecha.now().strftime(FECHA_FORMAT))

            # función para adicionar información fichero actlog.txt, le paso la fecha actual
            archivo_texto.adicionar_info_actlog(self.usuarios[pos], fecha_actual)

            # confirmo que el usuario se actualizo
            print(f'''
                    el usuario se ha actualizado exitosamente:
                    {self.usuarios[pos]}
                    ''')

        else:
            print(f'Tu edad es: {nuevos_datos.get("edad")}, debes ser mayor de edad para registrarte')

# _____________________________________________________________________________________

    def eliminar_usuario(self):

            # muestro los usuarios que están registrados hasta el momento
            self.mostrar_usuarios()
            
            print('\nIngrese la cédula del usuario a eliminar: ')
            cedula = ingresar_cedula_valida()
            pos = self.encontrar_posicion_usuario(cedula)

            print('\n-------- Usuario a Eliminar ----------')
            print(self.usuarios[pos])
            
            # elimino el usuario en la posición correspondiente y recupero el usuario eliminado
            usuario = self.usuarios.pop(pos)

            # muestro el usuario eliminado de la lista de usuarios
            print('\nEl siguiente usuario se eliminó exitosamente\n')
            print(usuario)
            
            # obtengo la fecha actual, año, mes, dia, hora, minuto, segundo, y la convierto a tipo datetime
            fecha_actual = convertir_str_a_datetime(fecha.now().strftime(FECHA_FORMAT))

            # función para adicionar información fichero elog.txt, le paso la fecha actual
            archivo_texto.adicionar_info_elog(usuario, fecha_actual)

# _____________________________________________________________________________________

# Métodos globales

# función para que validar que la fecha tenga el formato correcto, y no haya ingresado una fecha incorrecta, retorna el objeto tipo datetime
def ingresar_fecha_nacimiento_valida():

    # la única forma que rompa el bucle es que la fecha tenga un formato correcto, y una fecha pasada
    while True:
        fecha_nacimiento = input('Dime tu fecha de nacimiento con el siguiente formato (dd-mm-yyyy): ')
        try:
            #convertir la cadena a un objeto de fecha con el formato dado
            fecha_valida = fecha.strptime(fecha_nacimiento, "%d-%m-%Y").date()

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
# pruebas funciones 
if __name__ == '__main__':

    pass

    #Creo objeto
    usuario_1 = Usuario(id = 1, nombres = 'Alex', apellidos = 'Guitar', fecha_nacimiento='18-01-1979', edad=45)
    usuario_2 = Usuario(id = 2, nombres = 'Felipe', apellidos = 'Baterry', fecha_nacimiento='05-09-1998', edad=25)
    usuario_3 = Usuario(id = 3, nombres = 'Cuchito', apellidos= 'Cervecero', fecha_nacimiento='25-01-1964', edad=60)

    # fecha_nacimiento_str = '15-07-1990'
    # fecha_nacimiento = fecha.strptime(fecha_nacimiento_str, "%d-%m-%Y").date()
    # usuario_1.fecha_nacimiento = fecha_nacimiento
    # usuario_1.edad = usuario_1.calcular_edad()

    #creo una aerolinea
    aerolinea = Aerolinea()

    # añado usuarios a aerolinea, uso extend para agregar varios usuarios, en una lista
    aerolinea.usuarios.extend([usuario_1, usuario_2, usuario_3])

    # muestro todos los usuarios
    # aerolinea.mostrar_usuarios()

    # # busco un usuario y lo muestro
    # print(aerolinea.buscar_usuario(3))

    # registro usuario
    aerolinea.registrar_usuario()

    # actualizar usuario
    aerolinea.actualizar_usuario()
    
    # eliminar usuario
    aerolinea.eliminar_usuario()

    # buscar usuario
    # aerolinea.mostrar_usuario()

    # fecha_nacimiento_str = '15-07-1990'
    # fecha_nacimiento = fecha.strptime(fecha_nacimiento_str, "%d-%m-%Y").date()
    # print(f"La edad es: {calcular_edad(fecha_nacimiento)} años")

