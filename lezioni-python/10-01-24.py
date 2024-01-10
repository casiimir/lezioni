# Esercizio 1
# Scrivi un programma che conta il numero di parole presenti in una stringa
# Esercizio di conversione stringa a lista
##stringa = "Questo è un esempio di frase"
##
##stringa_lista = stringa.split(" ")
##
##totale_parole = len(stringa_lista)


# Esercizio 2
# Scrivi un programma che sostituisce tutte le vocali in una stringa
# con un carattere specificato

##stringa = "esempio di frase"
##carattere = "*"
##stringa_nuova = ""
##
##for c in stringa:
##    if(c == "a" or c == "e" or c == "i" or c == "o" or c == "u"):
##        stringa_nuova = stringa_nuova + carattere
##    else:
##        stringa_nuova = stringa_nuova + c
##
##print(stringa_nuova)


# Esercizio 3
# Scrivi un programma che calcola la somma di tutti in nuomeri in una lista
##
##lista = [1, 2, 3, 4, 5]
##somma = 0
##
##for x in lista:
##    somma = somma + x
##
##print(somma)


# Esercizio 4
# Scrivi un programma che sostituisca le parole con il numero di caratteri
# che contiene

##lista = ["mela", "pera", "ananas", "anguria"]
##lista_nuova = []
##
##for frutto in lista:
##    lista_nuova.append(len(frutto))
##
##print(lista_nuova)

# Esercizio 5
# Scrivere un programma che verifichi se il numero dato è un numero primo

##numero = 12
##
##if(numero % numero == 0 and numero / 1 == numero):
##    print(numero, "è un numero primo")

# Esercizio 6
# Scrivi un programma che identifica il numero che appare piu frequentemente
# in una lista

##lista = [1, 3, 3, 3, 2, 2, 4, 5]
##lista_numeri = []
##numero_frequenza = 0
##
##for x in lista:
##    if(x == 1):
##        lista_numeri.append([x])
##    

##lista = [1, 3, 3, 3, 2, 2, 4, 5]
##contatore = []
##
##for x in lista:
##    contatore.append([x, 1])
##
##print(contatore)


# Esercizio x

lista = [1, 2, 3, 4, 5, 6]
##contatore = 0
##
##for x in lista:
##    if(x % 2  != 0):
##        contatore = contatore + x

def somma_dispari(elementi):
    contatore = 0

    for x in elementi:
        if(x % 2  != 0):
            contatore = contatore + x

    return contatore


somma_dispari([2, 2, 2, 3, 4, 5,2,1,1,4,5,9])

somma_dispari([2, 2, 2, 3, 4, 5,21,1,1,4,5,12])
