
# importo datetime para las fechas
from datetime import datetime as fecha

class Usuario:

    # método constructor
    def __init__(self, id, nombres, apellidos, fecha_nacimiento, edad) -> None:
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__fecha_nacimiento = fecha_nacimiento
        self.__edad = edad
        self.__vuelo = None

    # método __str__()
    def __str__(self) -> str:

        if self.vuelo != None:
            return f'''
                    ---------- Usuario ----------
                    id = {self.__id}
                    nombres = {self.__nombres}
                    apellidos = {self.__apellidos}
                    fecha nacimiento = {self.__fecha_nacimiento}
                    edad = {self.__edad}
                    {self.__vuelo}
                    '''
        else:
            return f'''
                    ---------- Usuario ----------
                    id = {self.__id}
                    nombres = {self.__nombres}
                    apellidos = {self.__apellidos}
                    fecha nacimiento = {self.__fecha_nacimiento}
                    edad = {self.__edad}
                    vuelo = No adquirido
                    ''' 
    
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
        self.__fecha_nacimiento = fecha_nacimiento

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