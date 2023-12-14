"""
Guillem González Rodríguez
ASIXc 1C
14/12/2023


Programa que pinta per pantalla un taulell d'escacs marcat amb una B les caselles blanques, i amb una N les negres.
El programa, haurà de marcar amb * les caselles a les quals es pot moure una torre, des d'una posició concreta, que cal
demanar a l'usuari per la terminal. La posició ha de ser dos numeros de l'1 al 8 (ambdós inclosos).
Cal fer control d'errors.
"""

fila = int(input("Fila? "))
columna = int(input("Columna? "))


try:
    for n in range(1, 9):
        for m in range(1, 9):
            if m == columna or n == fila:
                print("*", end=" ")
            else:
                if (n % 2 == 0 and m % 2 != 0) or (n % 2 != 0 and m % 2 == 0):
                    print("N", end=" ")
                else:
                    print("B", end=" ")
        print("")

except:
    print("Error")
