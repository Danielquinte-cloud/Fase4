# =============================================================================
# PROYECTO: SOFTWARE FJ
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# GRUPO: 213023_373
# AUTOR: MIGUEL ANGEL FRANCO SUAREZ
# ARCHIVO: pruebas.py
# DESCRIPCION: PRUEBAS DEL SISTEMA
# =============================================================================

from modelos.cliente import Cliente
from modelos.asesoria import Asesoria
from modelos.reservaSala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.reserva import Reserva

# Inicialización de las listas para almacenar clientes, servicios y reservas.

clientes = []
servicios = []
reservas = []

# Pruebas funcionales del sistema mediante operaciones exitosas y fallidas

# OPERACIÓN 1: REGISTRO DE CLIENTE
# Se crea un cliente con información válida y se almacena en la lista.
# Resultado esperado: registro exitoso.

print("OPERACION 1")

try:
    cliente1 = Cliente(
        "C001",
        "Juan Perez",
        "juan@gmail.com",
        "3001234567"
    )

    clientes.append(cliente1)
    print("✅ Cliente registrado")

except Exception as e:
    print("❌", e)

# OPERACIÓN 2: CREACIÓN DE ASESORÍA
# Se crea una asesoría con información válida y se almacena en servicios.
# Resultado esperado: creación exitosa del servicio.

print("OPERACION 2")

try:

    asesoria1 = Asesoria(  
        "A001",
        "Python",
        50000,
        "medio"
    )

    servicios.append(asesoria1)

    print("✅ Asesoria creada")

except Exception as e:

    print("❌", e)  

# OPERACIÓN 3: CREACIÓN, CONFIRMACIÓN Y PROCESAMIENTO DE RESERVA
# Se crea una reserva asociando un cliente con un servicio.
# Posteriormente, se confirma y se procesa para calcular su costo.
# Resultado esperado: reserva procesada correctamente.

print("OPERACION 3 - CREACION Y PROCESAMIENTODE RESERVA")

try:

    reserva1 = Reserva(
        "R001",
        cliente1,
        asesoria1,
        2
    )

    reservas.append(reserva1)

    print("✅ Reserva Creada:", reserva1.estado)
    reserva1.confirmar()
    print("✅ Reserva Confirmada:", reserva1.estado)

    costo_reserva = reserva1.procesar()

    print("costo total de la reserva:", costo_reserva)
    print("esttado final:", reserva1.estado)

except Exception as e:

    print("❌", e)

# OPERACIÓN 4: VALIDACIÓN DE IDENTIFICADOR DUPLICADO
# Se intenta registrar un cliente con un identificador ya existente.
# Resultado esperado: el sistema debe impedir el registro duplicado.

print("OPERACION 4 - IDENTIFICADOR DUPLICADO")

try:

    cliente4 = Cliente(
        "C001",
        "Carlos Ruiz",
        "carlos@gmail.com",
        "3001112222"
    )

    for c in clientes:
        if c.identificador == cliente4.identificador:
            raise ValueError("Ya existe un cliente con ese identificador.")

    clientes.append(cliente4)

    print("✅ Cliente registrado")

except Exception as e:

    print("❌", e)

# OPERACIÓN 5: VALIDACIÓN DE NIVEL DE ASESORÍA
# Se intenta crear una asesoría con un nivel no permitido.
# Resultado esperado: el sistema debe rechazar la información.

print("OPERACION 5")

try:

    asesoria3 = Asesoria(
        "A003",
        "Redes",
        60000,
        "superexperto"
    )

    servicios.append(asesoria3)

    print("✅ Asesoria creada")

except Exception as e:

    print("❌", e)

# OPERACIÓN 6: CREACIÓN DE SALA
# Se crea una sala con capacidad y precio por hora establecidos.
# Resultado esperado: creación exitosa y almacenamiento en servicios.

print("OPERACION 6")

try:

    sala1 = ReservaSala(
        "S001",
        "Sala Principal",
        30,
        100000
    )

    servicios.append(sala1)

    print("✅ Sala creada")

except Exception as e:

    print("❌", e)

# OPERACIÓN 7: VALIDACIÓN DE CAPACIDAD
# Se intenta calcular el costo de una reserva para 50 personas,
# aunque la capacidad establecida para la sala es de 30.
# Resultado esperado: el sistema debe rechazar el sobrecupo.

print("OPERACION 7 - VALIDACION DE CAPACIDAD")

try:

    costo = sala1.calcular_costo(
        duracion=2,
        personas=50
    )

    print(costo)

except Exception as e:

    print("❌", e)    

# OPERACIÓN 8: CÁLCULO DE COSTO DE ASESORÍA
# Se calcula el costo de una asesoría con una duración de dos horas.
# Resultado esperado: cálculo exitoso del costo.

print("OPERACION 8")

try:

    costo = asesoria1.calcular_costo(
        duracion=2
    )

    print("✅ Costo:", costo)

except Exception as e:

    print("❌", e)
 
# OPERACIÓN 9: CREACIÓN DE ALQUILER DE EQUIPO
# Se crea un servicio de alquiler con sus características y valores.
# Resultado esperado: creación exitosa y almacenamiento en servicios.

print("OPERACION 9 - ALQUILER DE EQUIPO")

try:

    equipo1 = AlquilerEquipo(
        "E001",
        "Portatil Dell",
        "Computador",
        80000,
        50000,
        5
    )

    servicios.append(equipo1)

    print("✅ Equipo creado")

except Exception as e:

    print("❌", e)

# OPERACIÓN 10: CÁLCULO DE COSTO DE ALQUILER
# Se calcula el costo del alquiler teniendo en cuenta la duración
# y la cantidad de equipos solicitados.
# Resultado esperado: cálculo exitoso del costo.

print("OPERACION 10 - COSTO DE ALQUILER")

try:

    costo = equipo1.calcular_costo(
        duracion=3,
        cantidad=2
    )

    print("✅ Costo alquiler:", costo)

# Se imprimen los resultados
except Exception as e:

    print("❌", e)

   
# RESUMEN DE RESULTADOS
# Se muestran las cantidades de clientes, servicios y reservas almacenados.

print("\n===== RESUMEN =====")

print("Clientes almacenados:", len(clientes))
print("Servicios almacenados:", len(servicios))

print("\n========== RESUMEN ==========")

# ALMACENAMIENTO MEDIANTE OBJETOS Y LISTAS
# Se recorren las listas para mostrar la información de los objetos registrados.

print("\n===== ALMACENAMIENTO MEDIANTE OBJETOS Y LISTAS =====")

# Mostrar la información de los clientes registrados.
print("\nCLIENTES GUARDADOS")

for cliente in clientes:
    print(cliente.describir())

# Mostrar la información de los servicios registrados.
print("\nSERVICIOS GUARDADOS")

for servicio in servicios:
    print(servicio.describir())

# Mostrar el total de elementos almacenados en cada lista.
print("\nTotal clientes:", len(clientes))
print("Total servicios:", len(servicios))
print("Total reservas:", len(reservas))

# Consultar los nombres de los clientes registrados.
print("\nContenido de la lista clientes:")
for c in clientes:
    print("-", c.nombre)

# Consultar los identificadores de los servicios registrados.
print("\nContenido de la lista servicios:")
for s in servicios:
    print("-", s.identificador)

# Mostrar la información de las reservas almacenadas.
print("\nRESERVAS GUARDADAS")

for reserva in reservas:
    print(reserva.describir())

# Finalización de las pruebas del sistema.
print("\n===== FIN DE LAS PRUEBAS =====")
