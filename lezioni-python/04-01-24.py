# Esercizio 1
# Verifica se una stringa contiene solo numeri.
# Scrivi un programma che verifica se una stringa contiene solo numeri.
# stringa = "12345"

##stringa = "12345"
##sono_solo_numeri = False
##
##for c in stringa:
##    if(c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9"):
##        sono_solo_numeri = True
##    else:
##        sono_solo_numeri = False
##        break
##
##if(sono_solo_numeri):
##    print("Sono solo numeri!")
##else:
##    print("Non sono solo numeri!")


# Esercizio 2
# Inverti una stringa. Data una stringa, scrivi un programma
# che la inverte. stringa = "Python"

##stringa = "Python"
##stringa_nuova = ""
##contatore = -1
##
##for c in stringa:
##    stringa_nuova = stringa_nuova + stringa[contatore]
##    contatore = contatore - 1
##
##print(stringa_nuova)


# Esercizio 4
# Converti una lista di numeri in una stringa.
# Scrivi un programma che converte una lista di
# numeri interi in una stringa. lista = [1, 2, 3]

##lista = [1, 2, 3]
##stringa = ""
##
##for x in lista:
##    stringa = stringa + str(x)
##
##print(stringa)

# Esercizio 5
# Conta le vocali in una stringa.
# Scrivi un programma che conta il numero di vocali
# in una stringa. stringa = "esempio di frase"

##stringa = "esempio di frase"
##numero_vocali = 0
##
##for c in stringa:
##    if(c == "a" or c == "e" or c == "i" or c == "o" or c == "u"):
##        numero_vocali = numero_vocali + 1
##
##print("Il numero di vocali è: " + str(numero_vocali))


#Esercizio 6
# Calcola la media di una lista di numeri.
# Scrivi un programma che calcola la media
# di una lista di numeri. lista = [1, 2, 3, 4, 5]

##lista = [1, 2, 3, 4, 5]
##summa_valori = 0
##
##for x in lista:
##    summa_valori = summa_valori + x
##
##print(summa_valori / len(lista))

# Esercizio 7
# Trova il secondo numero più grande in una lista.
# Scrivi un programma che trova il secondo numero più
# grande in una lista di numeri. lista = [1, 3, 4, 5, 2]


# Esercizio 8
# Stampa la differenza tra gli elementi massimi e minimi
# di una lista. Scrivi un programma che calcola e
# stampa la differenza tra l'elemento più grande e
# quello più piccolo in una lista. lista = [1, 2, 3, 4, 5]

##lista = [1, 2, 3, 4, 5]
##max = 0
##min = lista[0]
##
##for x in lista:
##    if(x > max):
##        max = x
##
##    if(x < min):
##        min = x
##
##print(max - min)


