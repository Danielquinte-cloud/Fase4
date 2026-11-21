# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: MARIA YARITZA ROJAS PEÑA
# ARCHIVO: ENTIDAD.PY
# DESCRIPCION: CLASE ABSTRACTA BASE PARA CLIENTE, SERVICIO Y RESERVA
# =============================================================================

#Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod

class Entidad(ABC):
    # clase abstracta principal del sistema Software FJ. Sirve como base para las entidads del proyecto.

    def __init__ (self, identificador):
        # Constructor de la clase Entidad. Recibe y valida el identificador de cada objeto.

        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador no puede estar vacio.")

        self._identificador = identificador.strip()

    @property
    def identificador(self):
        #Permite consultar el identificador de la Entidad.

        return self._identificador

    @abstractmethod
    def describir(self):
        # Metodo abstracto que deben implementar las clases que hereden de Entidad.

        pass