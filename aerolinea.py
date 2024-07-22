
# importo datetime para las fechas
from datetime import datetime as fecha

class Aerolinea:

    # método constructor
    def __init__(self) -> None:
        self.__usuarios = []
        self.__archivo = None

    # métodos get
    @property
    def usuarios(self):
        return self.__usuarios
    
    @property
    def archivo(self):
        return self.__archivo

    