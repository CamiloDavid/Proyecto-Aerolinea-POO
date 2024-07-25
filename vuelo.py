
# importo datetime para las fechas
from datetime import datetime as fecha, date
# _____________________________________________________________________________________

class Vuelo:

    # método constructor
    def __init__(self, codigo, destino, precio, clase, fecha_vuelo):
        self.__codigo = codigo
        self.__destino = destino
        self.__precio = precio
        self.__clase = clase

        # para el atributo fecha_vuelo, pueden ocurrir 2 casos:
        # sea de tipo str, convierto tipo str a tipo datetime
        if isinstance(fecha_vuelo, str):
            self.__fecha_vuelo = fecha.strptime(fecha_vuelo, "%d-%m-%Y").date()
        # si es de tipo datetime, no hago ninguna conversión 
        elif isinstance(fecha_vuelo, date):
            self.__fecha_vuelo = fecha_vuelo
        else:
            raise ValueError("fecha_nacimiento debe ser una cadena en formato 'dd-mm-yyyy' o un objeto de tipo date")

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
            self.__fecha_vuelo = fecha.strptime(fecha_vuelo, "%d-%m-%Y").date()
        # si es de tipo datetime, no hago ninguna conversión 
        elif isinstance(fecha_vuelo, date):
            self.__fecha_vuelo = fecha_vuelo
        else:
            raise ValueError("fecha_nacimiento debe ser una cadena en formato 'dd-mm-yyyy' o un objeto de tipo date")

    # método destructor no es necesario definirlo