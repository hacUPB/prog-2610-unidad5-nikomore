nombre_archivo = input("Nombra tu nuevo archivo: ")
nombre_archivo +=".txt"

# Contexto de escritura
with open(nombre_archivo, 'w') as archivo:
    datos = input("Escribe tu primer secreto: ")
    archivo.write(datos)
    archivo.seek(0)
# Contexto de lectura
with open(nombre_archivo, 'r') as archivo:
    print("\n--- Leyendo tu archivo ---")
    print(archivo.read())