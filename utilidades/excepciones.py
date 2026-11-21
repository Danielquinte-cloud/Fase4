# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: KEVIN DANIEL QUINTERO JIMENEZ
# ARCHIVO: EXCEPCIONES.PY
# DESCRIPCION: EXCEPCIONES PERSONALIZADAS DEL SISTEMA SOFTWARE FJ
# =============================================================================


class ErrorSoftwareFJ(Exception):
    # Excepcion base del sistema. No se lanza directamente,
    # solo sirve para que las demas hereden de ella.
    pass


class DatoInvalidoError(ErrorSoftwareFJ):
    # Un dato general esta vacio o tiene un formato incorrecto.
    # Ejemplo: identificador vacio en la clase Entidad.
    pass


class ClienteInvalidoError(DatoInvalidoError):
    # Los datos del cliente estan mal.
    # Ejemplo: correo sin "@", documento con letras, nombre vacio.
    pass


class ServicioInvalidoError(DatoInvalidoError):
    # El servicio se intenta crear con datos incorrectos.
    # Ejemplo: precio negativo, tipo de servicio que no existe.
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    # Se intenta reservar un servicio que no esta disponible.
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    # La reserva no se puede crear o procesar.
    # Ejemplo: duracion en 0, reserva sin cliente o sin servicio.
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    # Se intenta hacer algo que no se puede en el estado actual.
    # Ejemplo: cancelar una reserva que ya estaba cancelada.
    pass


class CalculoInconsistenteError(ErrorSoftwareFJ):
    # El costo calculado no tiene sentido.
    # Ejemplo: descuento mayor al 100% o costo final negativo.
    pass