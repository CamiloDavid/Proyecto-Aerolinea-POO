
def adicionar_info_reglog(usuario, fecha_registro):

    try:
    # Abrir el archivo en modo append ('a')
        with open('reglog.txt', 'a', encoding='utf8') as file:
            # Escribir la línea en el archivo
            file.write(f'usuario: {usuario.id}, {usuario.nombres}, {usuario.apellidos}, registrado, {fecha_registro}\n')
        print("Información de usuario agregada a reglog.txt")
    except IOError as e:
        print(f"Error al abrir o escribir en el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# _____________________________________________________________________________________

def adicionar_info_actlog(usuario, fecha_actualizacion):

    try:
    # Abrir el archivo en modo append ('a')
        with open('actlog.txt', 'a', encoding='utf8') as file:
            # Escribir la línea en el archivo
            file.write(f'usuario: {usuario.id}, {usuario.nombres}, {usuario.apellidos}, actualizado, {fecha_actualizacion}\n')
        print("Información de usuario agregada a actlog.txt")
    except IOError as e:
        print(f"Error al abrir o escribir en el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# _____________________________________________________________________________________

def adicionar_info_elog(usuario, fecha_eliminacion):

    try:
    # Abrir el archivo en modo append ('a')
        with open('elog.txt', 'a', encoding='utf8') as file:
            # Escribir la línea en el archivo
            file.write(f'usuario: {usuario.id}, {usuario.nombres}, {usuario.apellidos}, eliminado, {fecha_eliminacion}\n')
        print("Información de usuario agregada a elog.txt")
    except IOError as e:
        print(f"Error al abrir o escribir en el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# _____________________________________________________________________________________

def adicionar_info_vtatlog(usuario, fecha_compra_tiquete):

    try:
    # Abrir el archivo en modo append ('a')
        with open('vtatlog.txt', 'a', encoding='utf8') as file:
            # Escribir la línea en el archivo
            file.write(f"""\nusuario: (cedula: {usuario.id}, {usuario.nombres}, {usuario.apellidos}),
            Vuelo : (clase: {usuario.vuelo.clase}, precio: {usuario.vuelo.precio}, fecha compra: {fecha_compra_tiquete}, 
            fecha vuelo: {usuario.vuelo.fecha_vuelo}, destino: {usuario.vuelo.destino})""")
        print("Información de usuario agregada a vtatlog.txt")
    except IOError as e:
        print(f"Error al abrir o escribir en el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")