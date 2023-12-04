# Funzione - fase 1 - Dichiarazione/Inizializzazione/Definizione
def first_char(string):  # Parametro
    # print(string[0])
    return string[0]  # Alla fine della esecuzione della funzione, il valore ritornato sarà string[0]


# Funzione - fase 2 - Invocazione/Esecuzione
first_char("Pippo")  # Argomento

pippo_first_char = first_char("Pippo")

# print(pippo_first_char)


# Dati tre numeri, fare la moltiplicazione tra loro. Creare una funzione
# che esegua questo compito. I numeri sono 3, 5, 10

# print(3 * 5 * 10)

def moltiplicazione(x, y, z):
    return (x * y * z)

risultato1 = moltiplicazione(3, 5, 10)

risultato2 = moltiplicazione(12, 5, 22)

risultato3 = moltiplicazione(1, 1, 1)

# Funzione di print personale
def stampa(string):
    print(string)

# stampa("Buongiorno")


# -------------------------- Istuzioni condizionali
# Espressioni booleane
##5 > 2 # true
##10 < 2 # false 
##10 >= 10 # true 
##10 <= 10 # true
##10 == 5 # false
##10 != 5 # true
##
##100 % 2 # 0 - 100 è divisibile per 2
##100 % 5 # 0 - 100 è divisibile per 5
##9 % 2 # 1 - 9 non è divisibile per 2
##9 % 3 # 0 - 9 è divisibile per tre

# Qualsiasi numero che da a modulo risultato 0 significa che è divisibile per quel numero

##n % 2 == 0 # pari
##n % 2 != 0 # dispari


def e_pari(x):
    return x % 2 == 0
 
# print(e_pari(11)) # False
# print(e_pari(10)) # True

# ----- IF - ELIF - ELSE ---------------

##oggi = input("Inserisci il giorno di oggi: ")
##
##if(oggi == 'lunedi' or oggi == 'Lunedi'):
##    print("Giornata difficile")
##elif(oggi == 'venerdi'):
##    print("Evviva è arrivato il fine settimana!")
##else:
##    print("Tutto sommato si va avanti")





