import random
concorso = {
    "Mario Rossi": [("atipasti", [8,7,9], "Junior Chef"), ("primi", [7,8,8], "Junior Chef"), ("secondi", [9,9,8], "Junior Chef"), ("dessert", [8,8,9], "Junior Chef")], 
    "Luigi Bianchi": [("atipasti", [7,7,8], "Senior Chef"), ("primi", [8,9,7], "Senior Chef"), ("secondi", [7,8,7], "Senior Chef"), ("dessert", [9,8,8], "Senior Chef")],
    "Giulia Verdi": [("atipasti", [9,8,8], "Junior Chef"), ("primi", [8,7,9], "Junior Chef"), ("secondi", [8,8,8], "Junior Chef"), ("dessert", [7,9,8], "Junior Chef")] 
}
#Nome Cognome, [[antipasti, (creatività, gusto, presentazione), categoria], [primi, (creatività, gusto, presentazione), categoria], [secondi, (creatività, gusto, presentazione), categoria], [dessert, (creatività, gusto, presentazione), categoria]]
concorso["Anna Bottini"] = [("antipasti", [6,7,8], "Junior Chef"), ("primi", [8,1,9], "Junior Chef"), ("secondi", [9,8,8], "Junior Chef"), ("dessert", [7,8,5], "Junior Chef")]


def stampa(nome):
    if(nome in concorso.keys()):
        for chef in concorso.keys():
            [antipasti, (creativita, gusto, presentazione), categoria], [primi, (creatività, gusto, presentazione), categoria], [secondi, (creatività, gusto, presentazione), categoria], [dessert, (creatività, gusto, presentazione), categoria] = concorso[chef]
            if(nome==chef):
                print(f"Categoria Chef: {categoria}")
                print(f"Nome e Cognome: {chef}")
                print(f"Punteggi antipasti: {concorso[chef][0][1]}")
                print(f"Creatività: {concorso[chef][0][1][0]}")
                print(f"Gusto: {concorso[chef][0][1][1]}")
                print(f"Presentazione: {concorso[chef][0][1][2]}")
print("Funzione stampa()")
nome=str(input("inserisci nome dello chef di cui vuoi visualizzarne i dati: "))
stampa(nome)

def aggiungiPiatto(nome):
    for chef in concorso.keys():
        concorso[chef]+=["piatti unici", [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)], "Senior Chef"]
print("Funzione AggiungiPiatto()")

def stampaPiatto(categoria):
    for chef in concorso.keys():
            [antipasti, (creativita, gusto, presentazione), categoria], [primi, (creatività, gusto, presentazione), categoria], [secondi, (creatività, gusto, presentazione), categoria], [dessert, (creatività, gusto, presentazione), categoria] = concorso[chef]
            if(categoria=="Senior Chef"):
                 print("Categoria Senior Chef: ")
                 print()
                 print(stampa(chef))
                 print()
            if(categoria=="Junior Chef"):
                 print("Categoria Junior Chef: ")
                 print()
                 print(stampa(chef))
                 print()
    else:
        print("Categoria non disponibile")
print("Funzione stampaPiatto()")
categoria=str(input("Inserisci la categoria di cui vuoi visualizzare il piatto: "))
stampaPiatto(categoria)


def totaleMax(concorso, categoriePiatto, categoriaChef):
    if(categoriePiatto in concorso[chef] and categoriaChef in concorso[chef]):
        for chef in concorso.keys():
            [piatto, (creativita, gusto, presentazione), categoria], [piatto, (creatività, gusto, presentazione), categoria], [piatto, (creatività, gusto, presentazione), categoria], [dessert, (creatività, gusto, presentazione), categoria] = concorso[chef]
            if(categoriePiatto==piatto and categoriaChef==categoria):
                somma=creativita+gusto+presentazione
                if(somma>max):
                    max=somma
    else: 
        print("Errore! Dati inseriti non validi")
    somma=0
    for chef in concorso.keys():
        [piatto, (creativita, gusto, presentazione), categoria], [piatto, (creatività, gusto, presentazione), categoria], [piatto, (creatività, gusto, presentazione), categoria], [dessert, (creatività, gusto, presentazione), categoria] = concorso[chef]
        if(somma==(creativita+gusto+presentazione)):
            print("Chef che hanno ottenuto max ", max)
            print(chef)

print("Funzione totaleMax")
categoriePiatto=str(input("Inserisci categoria del piatto: "))
categoriaChef=str(input("Inserisci categoria chef: "))
totaleMax(concorso, categoriePiatto, categoriaChef)

def mediaTot(concorso, categoriePiatto, categoriaChef):
    i=0
    for chef in concorso.keys():
        [piatto, (creativita, gusto, presentazione), categoria], [piatto, (creatività, gusto, presentazione), categoria], [piatto, (creatività, gusto, presentazione), categoria], [dessert, (creatività, gusto, presentazione), categoria] = concorso[chef]
        if(categoriePiatto==piatto and categoriaChef==categoria):
            media+=creativita+gusto+presentazione
            i+=1
    media/=i
    return media
print("Funzione mediaTot()")
categoriePiatto=str(input("Inserisci categoria del piatto: "))
categoriaChef=str(input("Inserisci categoria chef: "))
mediaTot(concorso, categoriePiatto, categoriaChef)

def inserisci_dati_nuovo_chef():
    #Nome Cognome, [[antipasti, (creatività, gusto, presentazione), categoria], [primi, (creatività, gusto, presentazione), categoria], [secondi, (creatività, gusto, presentazione), categoria], [dessert, (creatività, gusto, presentazione), categoria]]
    for i in range (4):
        while(True):
            creativita=str(input("Inserisci creatività di ", concorso[i][0]))
            if(creativita>1 and creativita<10):
                break
        while(True):
            gusto=str(input("Inserisci gusto di ", concorso[i][0]))
            if(gusto>1 and gusto<10):
                break
        while(True):
            presentazione=str(input("Inserisci presentazione di ", concorso[i][0]))
            if(presentazione>1 and presentazione<10):
                break
