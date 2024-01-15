# Esercizio 1
# Consegna: Scrivi una funzione che accetta una stringa come argomento e
# restituisce il numero di parole presenti in quella stringa.

def num_parole(string):
    lista_parole = string.split()
    return len(lista_parole)


# Esercizio 2
# Consegna: Crea una funzione che prende due argomenti: una stringa
# e un carattere. La funzione deve sostituire tutte le vocali nella
# stringa con il carattere specificato e restituire la nuova stringa.

def sostituzione(string, char):
    nuova_stringa = ""

    for x in string:
        if(x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
            nuova_stringa = nuova_stringa + char
        else:
            nuova_stringa = nuova_stringa + x

    return nuova_stringa

# Esercizio 3
# Consegna: Implementa una funzione che calcola la somma di tutti i
# numeri presenti in una lista fornita come argomento.

def somma(lista):
    somma_totale = 0
    
    for x in lista:
        somma_totale = somma_totale + x

    return somma_totale


# Esercizio 4
# Consegna: Scrivi una funzione che prende in input una lista di stringhe
# e restituisce una lista dei numeri corrispondenti alla lunghezza di
# ogni stringa.


def sostituzione_stringa(frutti):
    lista = []

    for x in frutti:
        lista.append(len(x))

    return lista


# Esercizio 5
# Consegna: Scrivi una funzione che, data una lista di numeri, somma i
# soli numeri pari e maggiori di 4 della lista e stampa il risultato.

def somma_pari(lista):
    somma = 0
    
    for x in lista:
        if(x % 2 == 0 and x > 4):
            somma = somma + x

    return somma


# Esercizio 6
# Consegna: Implementa una funzione che prende una lista di numeri e
# restituisce il numero pari più grande presente nella lista.

def pari_maggiore(lista):
    maggiore_pari = 0

    for x in lista:
        if(x % 2 == 0 and x > maggiore_pari):
            maggiore_pari = x

    return maggiore_pari

# Esercizio 7
# Consegna: Crea una funzione che, data una lista di numeri e un numero
# limite, conta quanti elementi nella lista sono minori del limite.


# Risultato atteso: [1, 4, 12, 5, 2] - 6 = 4

def minore_limite(lista, limite):
    contatore = 0

    for x in lista:
        if(x < limite):
            contatore = contatore + 1

    return contatore


# Esercizio 8
# Consegna: Scrivi una funzione che riceve in input una lista di numeri
# e restituisce una nuova lista contenente solo i numeri positivi.


def numeri_positivi(lista):
    lista_positivi = []

    for x in lista:
        if(x > 0):
            lista_positivi.append(x)

    return lista_positivi

# Esercizio 10
# Consegna: Crea una funzione che prende una lista di numeri e restituisce
# una nuova lista con gli stessi elementi in ordine inverso, escludendo i
# numeri divisibili per 3.

def reverse(lista):
    lista_nuova = []
    contatore = -1

    for x in lista:
        if(lista[contatore] % 3 == 0):
            lista_nuova.append(lista[contatore])
        contatore = contatore - 1

    return lista_nuova


# Esercizio 3 - ciclo while
# Consegna: Implementa una funzione che calcola la somma di tutti i
# numeri presenti in una lista fornita come argomento.

def somma(lista):
    somma_totale = 0
    contatore = 0 # 1. Il while ha bisogno sempre di un contatore 
    
    while(contatore < len(lista)):
        somma_totale = somma_totale + lista[contatore]
        contatore = contatore + 1 # 2. Il contatore deve essere incrementato
    

    return somma_totale


        
