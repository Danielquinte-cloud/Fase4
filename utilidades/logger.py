# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: KEVIN DANIEL QUINTERO JIMENEZ
# ARCHIVO: LOGGER.PY
# DESCRIPCION: REGISTRO DE EVENTOS Y ERRORES EN EL ARCHIVO logs/sistema.log
# =============================================================================


import logging
import os

# La carpeta logs se crea al lado de main.py (en la raiz del proyecto)
CARPETA_PROYECTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA_LOGS = os.path.join(CARPETA_PROYECTO, "logs")
os.makedirs(CARPETA_LOGS, exist_ok=True)
ARCHIVO_LOG = os.path.join(CARPETA_LOGS, "sistema.log")

# Configuramos el registro: fecha | tipo | mensaje
_logger = logging.getLogger("SoftwareFJ")
_logger.setLevel(logging.INFO)

# Este "if" evita que las lineas se repitan si el archivo se importa varias veces
if not _logger.handlers:
    _manejador = logging.FileHandler(ARCHIVO_LOG, encoding="utf-8")
    _manejador.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s",
                          datefmt="%Y-%m-%d %H:%M:%S")
    )
    _logger.addHandler(_manejador)


def registrar_evento(mensaje):
    # Anota algo que salio bien o que es importante (tipo INFO).
    _logger.info(mensaje)


def registrar_error(mensaje, excepcion=None):
    # Anota un error (tipo ERROR).
    # Si se le pasa la excepcion, anota tambien su nombre y su mensaje.
    # Si la excepcion viene encadenada (raise ... from e), anota la causa original.

    if excepcion is not None:
        mensaje = f"{mensaje} -> {type(excepcion).__name__}: {excepcion}"

        causa = excepcion.__cause__
        if causa is not None:
            mensaje += f" | Causa original: {type(causa).__name__}: {causa}"

    _logger.error(mensaje)