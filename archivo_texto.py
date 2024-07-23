
from datetime import datetime
from usuario import Usuario

def adicionar_info_reglog(usuario, fecha_registro):

    try:
    # Abrir el archivo en modo append ('a')
        with open('reglog.txt', 'a', encoding='utf8') as file:
            # Escribir la línea en el archivo
            file.write(f'usuario: {usuario.id}, {usuario.nombres}, {usuario.apellidos}, registrado, {fecha_registro}\n')
        print("Línea agregada correctamente.")
    except IOError as e:
        print(f"Error al abrir o escribir en el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")


def adicionar_info_actlog(usuario, fecha_actualizacion):

    try:
    # Abrir el archivo en modo append ('a')
        with open('actlog.txt', 'a', encoding='utf8') as file:
            # Escribir la línea en el archivo
            file.write(f'usuario: {usuario.id}, {usuario.nombres}, {usuario.apellidos}, actualizado, {fecha_actualizacion}\n')
        print("Línea agregada correctamente.")
    except IOError as e:
        print(f"Error al abrir o escribir en el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")


