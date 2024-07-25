# en caso de que el usuario no esté registrado, bloquearé todas las opciones a excepción de registrar usuario,
# con la anterior validación, sabré si el usuario si estaba registrado, entonces veo conveniente usar una bandera,
# si el usuario ya estaba registrado, bloquearé la opción de registrar usuario, y permitiré las demás opciones

# también bloquearé todas las opciones a excepción de la primera si no hay nada de usuarios registrados

# también para los vuelos, validar si el usuario no tiene adquirido vuelo, bloquear las opciones de actualizar vuelo,
# eliminar vuelo, mostrar vuelo, si el usuario tiene adquirido un vuelo, bloquear la primera opción de comprar vuelo, y desbloquear las otras dos opciones

import usuario
import vuelo
from aerolinea import *

# en este modulo estarán los menús de usuarios y vuelos

def mostrar_menu_principal(aerolinea: Aerolinea):
    while True:

        print(f'''
            ------- M E N Ú  P R I N C I P A L -------
            1. Menú Usuario
            2. Menú Vuelo
            3. Salir
            ------------------------------------------
        ''')

        try:
            opc = int(input('Dime una opción: '))

            if opc == 1:
                mostrar_menu_usuario(aerolinea)
            elif opc == 2:
                
                # valido que no entre al menú de vuelo, si no hay usuarios registrados y sin vuelos
                if aerolinea.usuarios:
                    if aerolinea.averiguar_vuelos_usuarios():
                        mostrar_menu_vuelo()
                    else:
                        print('\nNo hay vuelos adquiridos')
                else:
                    print('\nNo hay usuarios registrados')
                
            elif opc == 3:
                print('\nFue un gusto atenderte, adioooos =)')
                break
            else:
                print('Ingresó una opción incorrecta, vuelva a intentarlo')
                
        except ValueError as e:
            print(f'Error: {e}, ingresó un valor no entero, vuelva a intentarlo')


def mostrar_menu_usuario(aerolinea: Aerolinea):

    while True:
        
        # verifico si hay o no usuarios registrados
        if aerolinea.usuarios:
            b = 1 # si hay
        else:
            b = 0 # si no hay

        print(f'''
            ------- M E N Ú  U S U A R I O -------
            1. Registrar Usuario
            2. Actualizar Usuario
            3. Eliminar Usuario
            4. Consultar Usuario
            5. Consultar Usuarios
            6. Regresar a menú principal
            --------------------------------------
        ''')

        try:
            opc = int(input('Dime una opción: '))

            if opc == 1:
                aerolinea.registrar_usuario()

            # si ingreso una opción entre 2 y 5
            if 2 < opc < 6:
                # con ésta condición valido que si haya usuarios registrados
                if b == 1:
                    # valido que el usuario si esté registrado
                    cedula = globalfunc.ingresar_cedula_valida()
                    if aerolinea.buscar_usuario(cedula) != None:
                        if opc == 2:
                            aerolinea.actualizar_usuario(cedula)
                        elif opc == 3:
                            aerolinea.eliminar_usuario(cedula)
                        elif opc == 4:
                            aerolinea.mostrar_usuario(cedula)
                    else:
                        print(f'\nEl usuario con id: {cedula} no está registrado')
                    if opc == 5:
                        usuario.mostrar_detalle_usuarios()
                else:
                    print('\nNo hay usuarios registrados aún')

            elif opc == 6:
                break
            else:
                print('Ingresó una opción incorrecta, vuelva a intentarlo')
                
        except ValueError as e:
            print(f'Error: {e}, ingresó un valor no entero, vuelva a intentarlo')


def mostrar_menu_vuelo(aerolinea: Aerolinea):
    while True:
        print(f'''
            ------- M E N Ú  V U E L O -------
            1. Comprar Vuelo
            2. Actualizar Vuelo
            3. Eliminar Vuelo
            4. Consultar Vuelo
            5. Consultar Vuelos
            6. Regresar a menú principal
            ----------------------------------
        ''')

        try:
            opc = int(input('Dime una opción: '))

            # valido que el usuario si esté registrado
            cedula = globalfunc.ingresar_cedula_valida()
            if aerolinea.buscar_usuario(cedula) != None:
                if opc == 1:
                    aerolinea.comprar_tiquete(cedula)
                elif opc == 2:
                    aerolinea.actualizar_vuelo(cedula)
                elif opc == 3:
                    aerolinea.eliminar_vuelo(cedula)
                elif opc == 4:
                    aerolinea.mostrar_vuelo(cedula)
            else:
                print(f'\nEl usuario con id: {cedula} no está registrado')
            
            if opc == 5:
                vuelo.mostrar_detalle_vuelos()
            elif opc == 6:
                break
            else:
                print('Ingresó una opción incorrecta, vuelva a intentarlo')
                
        except ValueError as e:
            print(f'Error: {e}, ingresó un valor no entero, vuelva a intentarlo')

aerolinea = Aerolinea()
mostrar_menu_principal(aerolinea)
