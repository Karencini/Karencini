def cargar_y_mostrar_sala():
    """Carga una sala específica desde el archivo y muestra su estado actual."""
    # Asegura que los datos más recientes estén cargados
    cargar_datos()  
    nombre_sala = input("Ingrese el nombre de la sala a cargar y mostrar: ")
    mostrar_sala(nombre_sala)

def reservar_asiento():
    """Permite reservar un asiento específico en una sala."""
    nombre_sala = input("Ingrese el nombre de la sala: ")
    if nombre_sala in salas:
        fila = int(input("Ingrese el número de fila: ")) - 1
        columna = int(input("Ingrese el número de columna: ")) - 1
        if salas[nombre_sala][fila][columna] == 'O':
            salas[nombre_sala][fila][columna] = 'X'
            guardar_datos()
            print("Asiento reservado exitosamente.")
        else:
            print("El asiento ya está reservado.")
    else:
        print("La sala no existe.")

