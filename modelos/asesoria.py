# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: KEVIN DANIEL QUINTERO JIMENEZ
# ARCHIVO: ASESORIA.PY
# DESCRIPCION: SERVICIO DE ASESORIAS ESPECIALIZADAS (HEREDA DE SERVICIO)
# =============================================================================


from modelos.servicio import Servicio


from utilidades.excepciones import ServicioInvalidoError, ReservaInvalidaError
from utilidades.validaciones import (validar_texto, validar_rango,
                                     aplicar_impuesto_y_descuento)


class Asesoria(Servicio):
    # Servicio de asesorias especializadas de Software FJ

    HORAS_MINIMAS = 1
    HORAS_MAXIMAS = 4
    RECARGOS = {"basico": 1.0, "medio": 1.3, "experto": 1.6}

    def __init__(self, identificador, especialidad, tarifa_hora, nivel="basico", disponible=True):

        # Inicializamos la clase padre (identificador y disponibilidad)
        super().__init__(identificador, disponible)

        # Validamos y guardamos los datos propios de la asesoria
        self._especialidad = validar_texto(especialidad, "especialidad", ServicioInvalidoError)
        self._tarifa_hora = validar_rango(tarifa_hora, 1, 100_000_000, "tarifa por hora", ServicioInvalidoError)

        nivel = validar_texto(nivel, "nivel", ServicioInvalidoError).lower()
        if nivel not in self.RECARGOS:
            raise ServicioInvalidoError(
                f"El nivel '{nivel}' no existe. Opciones: basico, medio o experto."
            )
        self._nivel = nivel

    @property
    def nivel(self):
        return self._nivel

    @property
    def tarifa_hora(self):
        return self._tarifa_hora


# VALIDAR PARAMETROS


    def validar_parametros(self, **parametros):
        # Revisa que la duracion este entre 1 y 4 horas.

        if "duracion" not in parametros:
            raise ReservaInvalidaError("Falta la duracion (en horas) para la asesoria.")

        validar_rango(parametros["duracion"], self.HORAS_MINIMAS, self.HORAS_MAXIMAS,
                      "duracion (horas)", ReservaInvalidaError)

        return True


# CALCULAR COSTO


    def calcular_costo(self, **parametros):
        # Formula: tarifa por hora x horas x recargo del nivel.
        # Luego impuesto y descuento si los hay.
        # Ejemplos de uso:
        #   asesoria.calcular_costo(duracion=2)
        #   asesoria.calcular_costo(duracion=2, descuento=0.10)

        self.validar_parametros(**parametros)

        horas = float(parametros["duracion"])
        costo_base = self._tarifa_hora * horas * self.RECARGOS[self._nivel]

        return aplicar_impuesto_y_descuento(
            costo_base,
            parametros.get("impuesto", 0.0),
            parametros.get("descuento", 0.0),
        )


# DESCRIBIR


    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return (f"[{self.identificador}] Asesoria en {self._especialidad} | "
                f"Nivel {self._nivel} | ${self._tarifa_hora:,.0f} por hora | {estado}")