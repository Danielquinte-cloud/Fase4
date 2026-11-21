# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: MARIA YARITZA ROJAS PEÑA
# ARCHIVO: SERVICIO.PY
# DESCRIPCION: CLASE ABSTRACTA BASE PARA LOS SERVICIOS DEL SISTEMA
# =============================================================================

# Importamos la clase abstracta Entidad
from modelos.entidad import Entidad

# Importamos abstractmethod para definir metodos abstractos
from abc import abstractmethod

class Servicio(Entidad):
    # Clase abstracta Servicio que hereda de entidad
    # Sirve como base para los diferentes servicios ofrecidos por el sistema Software FJ
    # Establece los metodos que deben implementar las clases ReservaSala, AlquilerEquipo y Asesoria

    def __init__(self, identificador, disponible=True):

        # Inicializamos el constructor de la clase padre
        super().__init__(identificador)
        self._disponible = disponible

    @property
    def disponible(self):
        # Permite consultar la disponibilidad del servicio.
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        # Permite cambiar la disponibilidad del servicio.
        if not isinstance(valor, bool):
            raise ValueError("La disponibilidad debe ser un True o False.")
        self._disponible = valor

    #==============================================================================
    # METODO ABSTRACTO CALCULAR COSTO 
    #==============================================================================

    @abstractmethod
    def calcular_costo(self, **parametros):
        # Metodo abstracto encargado de calcular el costo del servicio
        # Cada servicio implementara su propia formula de calculo
        pass

    #==============================================================================
    # METODO ABSTRACTO DESCRIBIR
    #==============================================================================

    @abstractmethod
    def describir(self):
        # Metodo abstracto encargado de proporcionar la descripcion y caracteristicas del servicio
        pass

    #==============================================================================
    # METODO ABSTRACTO PARA VALIDAR PARAMETROS
    #==============================================================================

    @abstractmethod
    def validar_parametros(self, **parametros):
        # Metodo abstracto encargado de validar los parametros necesarios para utilizar cada servicio
        pass

    