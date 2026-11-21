# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: KEVIN DANIEL QUINTERO JIMENEZ
# ARCHIVO: RESERVA.PY
# DESCRIPCION: CLASE RESERVA QUE UNE CLIENTE, SERVICIO, DURACION Y ESTADO
# =============================================================================


from modelos.entidad import Entidad
from modelos.cliente import Cliente
from modelos.servicio import Servicio


from utilidades.excepciones import (ErrorSoftwareFJ, ReservaInvalidaError,
                                    ServicioNoDisponibleError,
                                    OperacionNoPermitidaError,
                                    CalculoInconsistenteError)
from utilidades.logger import registrar_evento, registrar_error


class Reserva(Entidad):
    # Clase Reserva que hereda de Entidad.
    # Une un cliente con un servicio por una duracion determinada
    # y controla su estado: confirmar, cancelar y procesar.

    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    PROCESADA = "PROCESADA"

    def __init__(self, identificador, cliente, servicio, duracion, **detalles):
        # "detalles" son datos opcionales que necesitan algunos servicios:
        #   personas=10  -> para ReservaSala
        #   cantidad=2   -> para AlquilerEquipo

        # Iniciamos el constructor de la clase padre
        super().__init__(identificador)

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._detalles = detalles
        self._estado = Reserva.PENDIENTE
        self._costo_total = None

        # Si algo esta mal, se anota en el log y la reserva no se crea
        try:
            self.validar()
        except ErrorSoftwareFJ as e:
            registrar_error(f"No se pudo crear la reserva {self.identificador}", e)
            raise

        registrar_evento(f"Reserva {self.identificador} creada para "
                         f"{self._cliente.nombre} ({self._servicio.identificador})")


# PROPIEDADES (solo lectura)

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def costo_total(self):
        return self._costo_total


# VALIDAR


    def validar(self):
        # Revisa que la reserva tenga sentido antes de crearla.

        if not isinstance(self._cliente, Cliente):
            raise ReservaInvalidaError(
                f"La reserva {self.identificador} no tiene un cliente valido."
            )

        if not isinstance(self._servicio, Servicio):
            raise ReservaInvalidaError(
                f"La reserva {self.identificador} no tiene un servicio valido."
            )

        if not self._servicio.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self._servicio.identificador} no esta disponible."
            )

        # Cada servicio revisa la duracion a su manera (polimorfismo):
        # la sala acepta 1-8 horas, el equipo 1-30 dias, la asesoria 1-4 horas.
        self._servicio.validar_parametros(duracion=self._duracion, **self._detalles)

        return True


# CONFIRMAR (try/except/finally)


    def confirmar(self):
        # Pasa la reserva de PENDIENTE a CONFIRMADA.
        # El bloque "finally" se ejecuta SIEMPRE, salga bien o mal,
        # y deja anotado en el log como quedo la reserva.

        try:
            if self._estado != Reserva.PENDIENTE:
                raise OperacionNoPermitidaError(
                    f"La reserva {self.identificador} no se puede confirmar "
                    f"porque esta {self._estado}."
                )

            # Se revisa otra vez: el servicio pudo dejar de estar disponible
            if not self._servicio.disponible:
                raise ServicioNoDisponibleError(
                    f"El servicio {self._servicio.identificador} ya no esta disponible."
                )

            self._estado = Reserva.CONFIRMADA
            registrar_evento(f"Reserva {self.identificador} confirmada.")

        except ErrorSoftwareFJ as e:
            registrar_error(f"No se pudo confirmar la reserva {self.identificador}", e)
            raise

        finally:
            registrar_evento(f"Intento de confirmacion de {self.identificador} "
                             f"terminado. Estado actual: {self._estado}")


# CANCELAR


    def cancelar(self):
        # Solo se puede cancelar una reserva PENDIENTE o CONFIRMADA.

        if self._estado not in (Reserva.PENDIENTE, Reserva.CONFIRMADA):
            error = OperacionNoPermitidaError(
                f"La reserva {self.identificador} no se puede cancelar "
                f"porque esta {self._estado}."
            )
            registrar_error("Cancelacion rechazada", error)
            raise error

        self._estado = Reserva.CANCELADA
        registrar_evento(f"Reserva {self.identificador} cancelada.")


# PROCESAR


    def procesar(self, impuesto=0.0, descuento=0.0):
        # Calcula el costo final de la reserva. Solo si esta CONFIRMADA.
        # Ejemplos:
        #   reserva.procesar()
        #   reserva.procesar(impuesto=0.19)
        #   reserva.procesar(impuesto=0.19, descuento=0.10)

        if self._estado != Reserva.CONFIRMADA:
            error = OperacionNoPermitidaError(
                f"La reserva {self.identificador} no se puede procesar "
                f"porque esta {self._estado}. Primero debe confirmarse."
            )
            registrar_error("Procesamiento rechazado", error)
            raise error

        try:
            costo = self._servicio.calcular_costo(
                duracion=self._duracion,
                impuesto=impuesto,
                descuento=descuento,
                **self._detalles
            )

        except (CalculoInconsistenteError, ReservaInvalidaError) as e:
            # Anotamos en el log el error original del calculo
            registrar_error(f"Fallo al procesar la reserva {self.identificador}", e)

            # ENCADENAMIENTO: el error del calculo se convierte en un error
            # de la reserva, pero se guarda cual fue la causa original.
            raise ReservaInvalidaError(
                f"No se pudo procesar la reserva {self.identificador}."
            ) from e

        else:
            # Solo entra aqui si el calculo salio bien
            self._costo_total = costo
            self._estado = Reserva.PROCESADA
            registrar_evento(f"Reserva {self.identificador} procesada. "
                             f"Total: ${costo:,.2f}")
            return costo


# DESCRIBIR


    def describir(self):
        costo = f"${self._costo_total:,.0f}" if self._costo_total is not None else "Sin calcular"
        return (f"Reserva {self.identificador} | "
                f"Cliente: {self._cliente.nombre} | "
                f"Servicio: {self._servicio.identificador} | "
                f"Duracion: {self._duracion} | "
                f"Estado: {self._estado} | "
                f"Total: {costo}")