fp = open(".\\archivos\\ejercicio2.txt", "r", encoding="utf-8")
datos_1 = fp.readlines()
fp.close()
print(lista)

for linea in lista:
    print(linea)