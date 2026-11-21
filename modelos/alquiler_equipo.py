# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: KEVIN DANIEL QUINTERO JIMENEZ
# ARCHIVO: ALQUILER_EQUIPO.PY
# DESCRIPCION: SERVICIO DE ALQUILER DE EQUIPOS (HEREDA DE SERVICIO)
# =============================================================================


from modelos.servicio import Servicio

from utilidades.excepciones import ServicioInvalidoError, ReservaInvalidaError
from utilidades.validaciones import (validar_texto, validar_rango,
                                     aplicar_impuesto_y_descuento)


class AlquilerEquipo(Servicio):
    # Servicio de alquiler de equipos de Software FJ

    DIAS_MINIMOS = 1
    DIAS_MAXIMOS = 30

    def __init__(self, identificador, nombre_equipo, tipo_equipo, precio_dia,
                 deposito=0, unidades=1, disponible=True):

        # Inicializamos la clase padre (identificador y disponibilidad)
        super().__init__(identificador, disponible)

        # Validamos y guardamos los datos propios del equipo
        self._nombre_equipo = validar_texto(nombre_equipo, "nombre del equipo", ServicioInvalidoError)
        self._tipo_equipo = validar_texto(tipo_equipo, "tipo de equipo", ServicioInvalidoError)
        self._precio_dia = validar_rango(precio_dia, 1, 100_000_000, "precio por dia", ServicioInvalidoError)
        self._deposito = validar_rango(deposito, 0, 100_000_000, "deposito", ServicioInvalidoError)
        self._unidades = int(validar_rango(unidades, 1, 1000, "unidades", ServicioInvalidoError))

    @property
    def precio_dia(self):
        return self._precio_dia

    @property
    def unidades(self):
        return self._unidades


# VALIDAR PARAMETROS


    def validar_parametros(self, **parametros):
        # Revisa que la duracion este entre 1 y 30 dias
        # y que no se pidan mas equipos de los que hay.

        if "duracion" not in parametros:
            raise ReservaInvalidaError("Falta la duracion (en dias) para el alquiler de equipo.")

        validar_rango(parametros["duracion"], self.DIAS_MINIMOS, self.DIAS_MAXIMOS,
                      "duracion (dias)", ReservaInvalidaError)

        validar_rango(parametros.get("cantidad", 1), 1, self._unidades,
                      "cantidad de equipos", ReservaInvalidaError)

        return True


# CALCULAR COSTO


    def calcular_costo(self, **parametros):
        # Formula: (precio por dia x dias + deposito) x cantidad.
        # Luego impuesto y descuento si los hay.
        # Ejemplos de uso:
        #   equipo.calcular_costo(duracion=2)
        #   equipo.calcular_costo(duracion=2, cantidad=3)
        #   equipo.calcular_costo(duracion=2, cantidad=3, descuento=0.15)

        self.validar_parametros(**parametros)

        dias = float(parametros["duracion"])
        cantidad = int(float(parametros.get("cantidad", 1)))

        costo_base = (self._precio_dia * dias + self._deposito) * cantidad

        return aplicar_impuesto_y_descuento(
            costo_base,
            parametros.get("impuesto", 0.0),
            parametros.get("descuento", 0.0),
        )


# DESCRIBIR


    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return (f"[{self.identificador}] Equipo '{self._nombre_equipo}' ({self._tipo_equipo}) | "
                f"${self._precio_dia:,.0f} por dia + deposito ${self._deposito:,.0f} | "
                f"{self._unidades} unidades | {estado}")