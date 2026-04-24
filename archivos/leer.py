fp = open(".\\archivos\\ejercicio1.txt", "r", encoding="utf-8")
datos_1 = fp.readline()
print("Primera lectura:", datos_1)

datos_2 = fp.readline()
print("Segunda lectura;", datos_2)

datos_3 = fp.read()
print("Tercera lectura:", datos_3)
fp.close()
