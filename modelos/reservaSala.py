# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: KEVIN DANIEL QUINTERO JIMENEZ
# ARCHIVO: RESERVASALA.PY
# DESCRIPCION: SERVICIO DE RESERVA DE SALAS
# =============================================================================

from modelos.servicio import Servicio

from utilidades.excepciones import ServicioInvalidoError, ReservaInvalidaError
from utilidades.validaciones import (validar_texto, validar_rango,
                                     aplicar_impuesto_y_descuento)



class ReservaSala(Servicio):
    # Servicio de reserva de salas de Software FJ

    HORAS_MINIMAS = 1
    HORAS_MAXIMAS = 8

    def __init__(self, identificador, nombre_sala, capacidad, precio_hora, disponible=True):

        # Inicializamos la clase padre (identificador y disponibilidad)
        super().__init__(identificador, disponible)

        # Validamos y guardamos los datos propios de la sala
        self._nombre_sala = validar_texto(nombre_sala, "nombre de la sala", ServicioInvalidoError)
        self._capacidad = int(validar_rango(capacidad, 1, 500, "capacidad", ServicioInvalidoError))
        self._precio_hora = validar_rango(precio_hora, 1, 100_000_000, "precio por hora", ServicioInvalidoError)

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def precio_hora(self):
        return self._precio_hora

#Validar Parametros

    def validar_parametros(self, **parametros):
        # Revisa que la duracion este entre 1 y 8 horas
        # y que el numero de personas (si se envia) quepa en la sala.

        if "duracion" not in parametros:
            raise ReservaInvalidaError("Falta la duracion (en horas) para la reserva de sala.")

        validar_rango(parametros["duracion"], self.HORAS_MINIMAS, self.HORAS_MAXIMAS,
                      "duracion (horas)", ReservaInvalidaError)

        if "personas" in parametros:
            validar_rango(parametros["personas"], 1, self._capacidad,
                          "personas", ReservaInvalidaError)

        return True

#Calcular Costo

    def calcular_costo(self, **parametros):
        # Formula: precio por hora x horas. Luego impuesto y descuento si los hay.
        # Ejemplos de uso:
        #   sala.calcular_costo(duracion=3)
        #   sala.calcular_costo(duracion=3, impuesto=0.19)
        #   sala.calcular_costo(duracion=3, impuesto=0.19, descuento=0.10)

        self.validar_parametros(**parametros)

        costo_base = self._precio_hora * float(parametros["duracion"])

        return aplicar_impuesto_y_descuento(
            costo_base,
            parametros.get("impuesto", 0.0),
            parametros.get("descuento", 0.0),
        )

#Describir

    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return (f"[{self.identificador}] Sala '{self._nombre_sala}' | "
                f"Capacidad: {self._capacidad} personas | "
                f"${self._precio_hora:,.0f} por hora | {estado}")