"""
Guillem González Rodríguez
ASIXc 1C
14/12/2023


Programa que implementi la funcionalitat del mètode replace. (sense fer servir el mètode). És a dir un programa que
demani una cadena de caràcters, un caràcter a modificar i un altre caràcter de substitució.
No es pot fer servir cap funció predefinida de Python. Cal fer control d'errors.
"""

frase = str(input("Introdueix una frase: \n"))
frasesplit = frase.split()
replacee = input("Quin caràcter vols reemplaçar? \n")
replacement = input("Quin és el caràcter de substitució?\n")


try:
    for n in range(0, len(frase)):
        if frase[n] == replacee:
            print(replacement, end="")
        else:
            print(frase[n], end="")
except:
    print("Error")
