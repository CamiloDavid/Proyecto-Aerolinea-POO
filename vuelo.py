
# importo datetime para las fechas
from datetime import datetime as fecha, date
from uuid import uuid4 # de la librería uuid importo el método uuid4, para asignar códigos
# _____________________________________________________________________________________

# Definimos la constante para el formato de fecha al inicio del archivo
FECHA_FORMAT = "%d-%m-%Y"
# _____________________________________________________________________________________

class Vuelo:

    # método constructor
    def __init__(self, destino, precio, clase, fecha_vuelo):
        self.__codigo = str(uuid4()) # convierto el código a tipo string
        self.__destino = destino
        self.__precio = precio
        self.__clase = clase
        self.fecha_vuelo = fecha_vuelo  # Usamos el setter aquí, ya que tiene las validaciones

# _____________________________________________________________________________________

    # método __str__
    def __str__(self):
        return f'''
                -------- Vuelo --------
                Codigo = {self.__codigo}
                Destino = {self.__destino}
                Precio = {self.__precio}
                Clase = {self.__clase}
                Fecha vuelo = {self.__fecha_vuelo}
                '''
# _____________________________________________________________________________________

    # métodos get() y set()
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino):
        self.__destino = destino

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def clase(self):
        return self.__clase

    @clase.setter
    def clase(self, clase):
        self.__clase = clase

    @property
    def fecha_vuelo(self):
        return self.__fecha_vuelo

    @fecha_vuelo.setter
    def fecha_vuelo(self, fecha_vuelo):
        if isinstance(fecha_vuelo, str):
            try:
                self.__fecha_vuelo = fecha.strptime(fecha_vuelo, FECHA_FORMAT).date()
            except ValueError:
                raise ValueError(f"El formato de fecha debe ser '{FECHA_FORMAT}'")
        elif isinstance(fecha_vuelo, date):
            self.__fecha_vuelo = fecha_vuelo
        else:
            raise ValueError(f"fecha_vuelo debe ser una cadena en formato '{FECHA_FORMAT}' o un objeto de tipo date")

    # método destructor no es necesario definirlo