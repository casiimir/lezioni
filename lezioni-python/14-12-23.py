# Iterazione - WHILE

# n_times = 1 # Contatore (Indispensabile!)

# while(n_times <= 3):
    # print(n_times)
##    print("Inserisci il tuo nome: ")
##    name = input("")
##    print("Benvenuto", name)
    # n_times = n_times + 1 # Incremento contatore (Indispensabile!)


# Iterazione - FOR in range()
##for n_time in range(3):
##    print("Inserisci il tuo nome: ")
##    name = input("")
##    print("Benvenuto", name)



# Iterazione - FOR in LISTA

##canestro_frutta = ["pere", "kiwi", "arancia", "banana"]
##
##for frutto in canestro_frutta:
##    print(frutto)



# Verificare che una stringa sia palindroma - by input
stringa = input("Inserisci la parola da verificare: ")
cont = 1

for i in range(len(stringa)):
    if(stringa[i] != stringa[len(stringa) - cont]):
        print("La stringa non è palindroma")
        break;
    else:
        print("è palindroma!")
        cont = cont + 1
        
