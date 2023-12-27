# Esercizio 1
# Data la lista [1,2,3,4,5,6,7,8,9,10] scrivere un programma che separi
# i numeri pari da dispari in due liste distinte

##lista_numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##lista_numeri_pari = []
##lista_numeri_dispari = []
##
##for numero in lista_numeri:
##    if(numero % 2 == 0):
##        lista_numeri_pari.append(numero)
##    else:
##        lista_numeri_dispari.append(numero)
##
##
##print("La lista dei pari: ", lista_numeri_pari)
##print("La lista dei dispari: ", lista_numeri_dispari)


# Esercizio 2
# Data la lista [1, 2, 3, 4, 3, 2, 1, 3, 4, 3] e un elemento
# conta quante volte l'elemento è presente nella lista

##lista_numeri = [1, 2, 3, 4, 3, 2, 1, 3, 4, 3]
##elemento = input("Inserisci l'elemento: ")
##presente_n_volte = 0
##
##for numero in lista_numeri:
##    if(numero == int(elemento)):
##        presente_n_volte += 1
##
##print(presente_n_volte)


# Esercizio 3
# Data la lista [1, 2, 3, 4, 5], invertire l'ordine degli elementi
# senza utilizzare funzioni già incluse

##lista_numeri = [1, 2, 3, 4, 5]
##lista_numeri_invertiti = []
##indice = -1
##
##for numero in lista_numeri:
##    lista_numeri_invertiti.append(lista_numeri[indice])
##    indice -= 1
##
##print(lista_numeri_invertiti)

# import random

# # Crea un elemento random da 10 a 20
# elemento_random = random.randint(10, 20)

import turtle

disegno = turtle.Turtle()
disegno.shape("turtle")

# Disegna un triangolo
##disegno.forward(200)
##disegno.right(300)
##disegno.back(200)
##disegno.right(300)
##disegno.back(-200)

for n in range(200):
    disegno.forward(n)
    disegno.right(n + 5)
    if (n % 2 == 0):
        disegno.color("cyan")
    elif (n % 5 == 0):
        disegno.color("red")
        disegno.pensize(2)
    elif (n % 25 == 0):
        disegno.color("green")
        disegno.begin_fill()
        disegno.circle(100)
        disegno.end_fill()
    else:
        disegno.color("black")
        disegno.pensize(1)
        disegno.speed(10)
