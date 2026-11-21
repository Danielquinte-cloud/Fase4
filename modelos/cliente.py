# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: MARIA YARITZA ROJAS PEÑA
# ARCHIVO: CLIENTE.PY
# DESCRIPCION: CLASE ABSTRACTA BASE PARA CLIENTE, SERVICIO Y RESERVA
# =============================================================================

# Importamos la clase abstracta Entidad
from modelos.entidad import Entidad

# Importamos expresiones regulares para validar los datos
import re

class Cliente(Entidad):
# Clase cliente que hereda de Entidad. 
# Permite registrar clientes mediante atributos privados, 
# propiedades y validacion de datos personales.

    def __init__(self, identificador, nombre, correo, telefono):

        # Iniciamos el constructor de la clase padre
        super().__init__(identificador)

        # Asignamos los datos utilizando sus propiedades
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    #=============================================================================
    # PROPIEDAD NOMBRE
    #=============================================================================

    @property
    def nombre(self):
        # Permite consultar el nombre del cliente.
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # Valida que el nombre no este vacio y contenga letras.

        if not isinstance(valor, str):
            raise TypeError("El nombre debe ser un texto.")

        valor = valor.strip()

        if not valor:
            raise ValueError("El nombre no puede estar vacío.")

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", valor):
            raise ValueError("El nombre contiene caracteres no validos.")

        self.__nombre = valor

        #=============================================================================
        # PROPIEDAD CORREO ELECTRONICO
        #=============================================================================

    @property
    def correo(self):
        # Permite consultar el correo electrónico del cliente.
        return self.__correo

    @correo.setter
    def correo(self, valor):
        # Valida que el correo tenga un formato correcto.

        if not isinstance(valor, str):
            raise TypeError("El correo debe ser un texto.")

        valor = valor.strip()

        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.fullmatch(patron, valor):
            raise ValueError("El correo electrónico no es valido.")

        self.__correo = valor

    #=============================================================================
    # PROPIEDAD TELEFONO
    #=============================================================================

    @property
    def telefono(self):
        # Permite consultar el teléfono del cliente.
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        # Valida que el telefono tenga entre 7 y 15 digitos.

        if not isinstance(valor, str):
            raise TypeError("El teléfono debe ser un texto.")

        valor = valor.strip()

        # Permitimos espacios, parentesis, guiones y signo +
        if not re.fullmatch(r"[\d\s\(\)\-\+]+", valor):
            raise ValueError("El teléfono contiene caracteres no validos.")

        # Contamos solamente los digitos
        digitos = re.sub(r"\D", "", valor)

        if not 7 <= len(digitos) <= 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 dígitos.")

        self.__telefono = valor

        #=============================================================================
        # METODO ABSTRACTO HEREDADO DE ENTIDAD
        #=============================================================================

    def describir(self):
        # Implementación del método abstracto describir de la clase Entidad. 
        # Devuelve una descripción de la informacion del cliente.

        return(
            f"Cliente: {self.nombre} |"
            f"Identificador: {self.identificador} |"
            f"Correo: {self.correo} |"
            f"Teléfono: {self.telefono}"
        )