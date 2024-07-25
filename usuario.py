
# importo datetime para las fechas
from datetime import datetime as fecha, date
# _____________________________________________________________________________________

# Definimos la constante para el formato de fecha al inicio del archivo
FECHA_FORMAT = "%d-%m-%Y"
# _____________________________________________________________________________________

class Usuario:
# _____________________________________________________________________________________

    # método constructor
    def __init__(self, id=1, nombres='Pepito', apellidos='Pérez', fecha_nacimiento='01.01.2000', edad=24) -> None:
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento  # Usamos el setter aquí, ya que tiene las validaciones
        self.__edad = edad
        self.__vuelo = None

# _____________________________________________________________________________________

    # método __str__(), uso validación para imprimir en consola si el vuelo se ha adquirido imprimirlo
    # de lo contrario imprimir "Aún no adquirido"

    def __str__(self) -> str:
        usuario_info = {
            "id": self.__id,
            "nombres": self.__nombres,
            "apellidos": self.__apellidos,
            "fecha nacimiento": self.__fecha_nacimiento.strftime(FECHA_FORMAT),
            "edad": self.__edad,
            "vuelo": self.__vuelo if self.__vuelo is not None else "Aún no adquirido"
        }

        return "\n".join([
            "\n---------- Usuario ----------",
            # por cada key-value, imprimir cada par
            *[f"{key} = {value}" for key, value in usuario_info.items()],
            ""
        ])
# _____________________________________________________________________________________

    # métodos get y set()
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombres(self):
        return self.__nombres
    
    @nombres.setter
    def nombres(self, nombres):
        self.__nombres = nombres

    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        if isinstance(fecha_nacimiento, str):
            try:
                self.__fecha_nacimiento = fecha.strptime(fecha_nacimiento, FECHA_FORMAT).date()
            except ValueError:
                raise ValueError(f"El formato de fecha debe ser '{FECHA_FORMAT}'")
        elif isinstance(fecha_nacimiento, date):
            self.__fecha_nacimiento = fecha_nacimiento
        else:
            raise ValueError(f"fecha_nacimiento debe ser una cadena en formato '{FECHA_FORMAT}' o un objeto de tipo date")

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
        
    @property
    def vuelo(self):
        return self.__vuelo
    
    @vuelo.setter
    def vuelo(self, vuelo):
        self.__vuelo = vuelo

    # método destructor no es necesario definirlo

    # métodos mios

# _____________________________________________________________________________________

if __name__ == '__main__':
    # pruebo método get

    usuario_1 = Usuario(id = 2, nombres = 'Camilo')

    usuario_1.apellidos = 'David'
    # apellido_modificado = usuario_1.apellidos/
    print('\n',usuario_1.apellidos)
    print(usuario_1.id)
    print(usuario_1.nombres)
    print(usuario_1.edad)
    print(usuario_1.fecha_nacimiento)
    
    print(usuario_1)
