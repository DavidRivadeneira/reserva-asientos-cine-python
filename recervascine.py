# Tarea: Reserva de un asiento en sala de cine (3 filas x 4 columnas)
# 0 = libre, 1 = reservado

FILAS = 3
COLUMNAS = 4

# 1) Crear matriz 3x4 con ceros
asientos = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# 2) Pedir fila y columna (con validación)
while True:
    try:
        f = int(input("Ingrese fila (0 a 2): "))
        if 0 <= f <= 2:
            break
        print("Error: la fila debe estar entre 0 y 2.")
    except ValueError:
        print("Error: ingrese un número entero.")

while True:
    try:
        c = int(input("Ingrese columna (0 a 3): "))
        if 0 <= c <= 3:
            break
        print("Error: la columna debe estar entre 0 y 3.")
    except ValueError:
        print("Error: ingrese un número entero.")

# 3) Reservar el asiento
if asientos[f][c] == 1:
    print("Ese asiento ya está reservado.")
else:
    asientos[f][c] = 1
    print("Asiento reservado con éxito.")

# 4) Mostrar la matriz en formato tabla usando bucles anidados
print("\nEstado de la sala:")
for i in range(FILAS):
    for j in range(COLUMNAS):
        print(asientos[i][j], end=" ")
    print()  # salto de línea al terminar la fila