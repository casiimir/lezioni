# SINTASSI IF

# keyword(condizione):
#   # blocco codice

# eta = input("Inserisci la tua età:")

##if(int(eta) > 18 and int(eta) != 54 and int(eta) != 100):
##    print("Accesso consentito")
##    # codice ...
##elif (int(eta) == 18 or int(eta) == 100):
##    print ("Aspetta e spera")
##elif (int(eta) == 54):
##    print("Hai vinto un bonus")
##elif (int(eta) == 5):
##    print("Ne hai ancora da crescere")
##else:
##    print("Vietato accesso")
    

# IF CON INTERVALLO
# Scrivere un if che controlla uno dei 3 stati: bambino(14) - ragazzo(18) - adulto - vecchietto (70)
##if(int(eta) <= 14):
##    print("Bambino")
##elif(int(eta) > 14 and int(eta) < 18):
##    print("Ragazzo")
##elif(int(eta) >= 70):
##    print("Vecchietto")
##else:
##    print("Adulto")

# IF ANNIDATO - aggiungere infante (3)
##if(int(eta) <= 14):
##    if(int(eta) <= 3):
##        print("infante")
##    else:
##        print("bambino")
##elif(int(eta) > 14):
##    if(int(eta) < 18):
##        print("ragazzo")
##    elif(int(eta) >= 18):
##        if(int(eta) < 70):
##            print("adulto")
##        else:
##            print("vecchietto")


# STRINGHE - gli indici definiscono la posizione di un determinato carattere nella sua stringa
name = "Pippo"
mood = "Oggi mi sento davvero bene!"

# print(mood[9])
# print(mood[-2]) ## Va in negativo e quindi sarà: e
# print(len(mood))
# print(mood[8:14]) ## Intervalli di partenza e di fine


# LISTE - utili per memorizzare piu di un valore
fruits = ["mela", "pera", "kiwi", "arancia"]
print(fruits) # Stampa tutta la lista
print(fruits[2]) # Stampa solo kiwi
print(fruits[2][2]) # Stampa di kiwi solo la w

# Metodo classico senza lista
cart1 = "iphone"
cart2 = "macbook"
cart3 = "smarthwatch"

# Metodo con lista
cart = ["iphone", "macbook", "smartwatch"]

print(cart[0])

