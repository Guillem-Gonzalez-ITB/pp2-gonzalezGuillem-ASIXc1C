"""
Guillem González Rodríguez
ASIXc 1C
14/12/2023


L'usuari introduirà una llista d'enters separada per espais. Previament dirà quants enters introduirà.
Un cop llegits tots, mostrar per pantalla la suma de tots els valors positius.
Cal fer control d'errors
"""
numnumeros = int(input())
numeros = str.split(input(), sep=" ")
record = 0


try:
    for n in range(0, numnumeros):
        if int(numeros[n]) > 0:
            record += int(numeros[n])

    print(record)
except:
    print("Error")
