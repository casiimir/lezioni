# Esercizio 1 - Calcola la somma di tutti gli elementi in una lista. lista = [11, 2, 6, 4, 8]

##lista = [11, 2, 6, 4, 8]
##sum = 0
##lista_somma_finale = []
##
##for x in lista:
##    sum = sum + x
##
##print(sum)
##lista_somma_finale.append(sum)
##print(lista_somma_finale)

# Esercizio 2 - Trova il numero più grande in una lista di numeri. lista = [11, 2, 6, 4, 8]

##lista = [11, 2, 66, 4]
##numero_maggiore = 0
##
##for x in lista:
##    if(x > numero_maggiore):
##        numero_maggiore = x
##
##print(numero_maggiore)


# Esercizio  3 - Data una lista, stampa tutti i numeri pari. lista = [1, 2, 3, 4, 5, 6]

##lista = [1, 2, 3, 4, 5, 6]
##
##for x in lista:
##    if(x % 2 == 0):
##        print(x)


# Esercizio 4 - Trova il numero minore in una lista di numeri. lista = [7, 2, 8, 4, 3]

##lista = [7, 2, 8, 4, 3, 1]
##numero_minore = lista[0]
##
##for x in lista:
##    if(x < numero_minore):
##        numero_minore = x
##
##print(numero_minore)


# Esercizio 5 - Data una lista di numeri da 1 a 100, stampa tutti quelli che sono multipli sia di 3 che di 5.

##for x in range(1, 101):
##    if(x % 3 == 0 and x % 5 == 0):
##        print(x)



# Esercizio 6 - Data la seguente lista di caratteri,
# stampare quante occorrenze della lettera 'a' sono presenti

##lista = ['f', 'd', 'e', 'a', 'b', 'a', 'l', 'p','o','a', 'd']
##numero_occorrenze = 0
##
##for x in lista:
##    if(x == 'a'):
##        numero_occorrenze = numero_occorrenze + 1
##
##print(numero_occorrenze)

# Esercizio 7 - Data la seguente lista di caratteri,
# stampare quante occorrenze della lettera chiesta all'utente

##lettera_utente = input("Inserire il carattere: ")
##lista = ['f', 'd', 'e', 'a', 'b', 'a', 'l', 'p','o','a', 'd']
##n_occorrenze = 0
##
##for c in lista:
##    if(c == lettera_utente):
##        n_occorrenze = n_occorrenze + 1
##
##print(n_occorrenze)


# Esercizio 8 - Data una stringa di testo, verificare quante occorrenze della
# lettera scelta dall'utente, sono prensenti

##stringa = "Buongiorno a tutti, oggi è proprio una bella giornata!"
##scelta_utente = input("Inserisci una lettera: ")
##n_occorrenze = 0
##
##for c in stringa:
##    if(c == scelta_utente):
##        n_occorrenze = n_occorrenze + 1
##
##
##print(n_occorrenze)

# Esercizio 9 - data una lista di frutti, stampare il frutto la cui
# lunghezza di lettere è la maggiore

##lista_frutti = ['mela', 'pera', 'kiwi', 'ananas', 'banana', 'arancia', 'anguria']
##parola_piu_lunga = ""
##
##for x in lista_frutti:
##    if(len(x) > len(parola_piu_lunga)):
##        parola_piu_lunga = x
##
##print(parola_piu_lunga)

# Esercizio 10 - data una lista di frutti, stampare il frutto la cui
# lunghezza di lettere è la maggiore e che processi fino all'ultimo elemento=

##lista_frutti = ['mela', 'pera', 'kiwi', 'ananas', 'banana', 'arancia', 'anguria']
##parola_piu_lunga = ""
##
##for x in lista_frutti:
##    if(len(x) >= len(parola_piu_lunga)):
##        parola_piu_lunga = x
##
##print(parola_piu_lunga)
