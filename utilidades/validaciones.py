# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: KEVIN DANIEL QUINTERO JIMENEZ
# ARCHIVO: VALIDACIONES.PY
# DESCRIPCION: FUNCIONES DE APOYO PARA VALIDAR DATOS Y CALCULAR COSTOS
# =============================================================================


from utilidades.excepciones import CalculoInconsistenteError


# CONVERTIR A NUMERO


def convertir_a_numero(valor, nombre_campo, tipo_error):
    # Intenta convertir el valor a numero.
    # Si no se puede (por ejemplo "abc" o None), atrapa el error de Python
    # y lanza en su lugar una excepcion propia del sistema, guardando
    # la causa original con "from e" (encadenamiento de excepciones).

    try:
        numero = float(valor)
    except (TypeError, ValueError) as e:
        raise tipo_error(
            f"El campo '{nombre_campo}' debe ser un numero. Se recibio: {valor!r}"
        ) from e

    return numero



# VALIDAR RANGO


def validar_rango(valor, minimo, maximo, nombre_campo, tipo_error):
    # Convierte el valor a numero y revisa que este entre minimo y maximo.
    # Si no cumple, lanza el tipo de error que se le indique.

    numero = convertir_a_numero(valor, nombre_campo, tipo_error)

    if numero < minimo or numero > maximo:
        raise tipo_error(
            f"El campo '{nombre_campo}' debe estar entre {minimo} y {maximo}. Se recibio: {numero:g}"
        )

    return numero



# VALIDAR TEXTO


def validar_texto(valor, nombre_campo, tipo_error):
    # Revisa que el valor sea un texto y que no este vacio.

    if not isinstance(valor, str) or not valor.strip():
        raise tipo_error(f"El campo '{nombre_campo}' no puede estar vacio.")

    return valor.strip()



# APLICAR IMPUESTO Y DESCUENTO


def aplicar_impuesto_y_descuento(costo_base, impuesto=0.0, descuento=0.0):
    # Recibe el costo base y le aplica impuesto y descuento, si los hay.
    # Los dos se escriben en decimal: 0.19 = 19%, 0.10 = 10%.
    #
    # Gracias a los parametros opcionales, la misma funcion sirve para:
    #   - costo sin impuesto ni descuento
    #   - costo con impuesto
    #   - costo con descuento
    #   - costo con los dos

    impuesto = validar_rango(impuesto, 0, 1, "impuesto", CalculoInconsistenteError)
    descuento = validar_rango(descuento, 0, 1, "descuento", CalculoInconsistenteError)

    costo_final = costo_base * (1 - descuento) * (1 + impuesto)

    # Revision final: un costo negativo o en cero no tiene sentido
    if costo_final <= 0:
        raise CalculoInconsistenteError(
            f"El costo calculado no es valido: {costo_final:,.2f}"
        )

    return round(costo_final, 2)