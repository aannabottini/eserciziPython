#("citta", [("mese1", valore1),("mese2", valore2), ..])
valoriPluviometrici=(
    ("Roma", [("Gennaio", 9), ("Febbraio", 11), ("Giugno", 23)]),
    ("Milano", [("Gennaio", 7), ("Febbraio", 8), ("Giugno", 30), ("Luglio", 30)]),
)
#print(len(valoriPluviometrici))
def datiPrecipitazioni(nomeCitta):
    somma=0
    #print(nomeCitta)
    for citta, rilevazioni in valoriPluviometrici: 
        #print("Sono nel ciclo")
        #print(rilevazioni)
        if(nomeCitta==citta):
            #print(nomeCitta, "", citta)
            
            #print(rilevazioni)
            max=0
            min=10000
            mesiMax=[]
            mesiMin=[]
            for mese, valore in rilevazioni: 
                somma+=valore #somma per media;
                if(valore>max): #calcolo valore max
                    max=valore 
                if(valore<min): #calcolo valore min
                    min=valore
            for mese, valore in rilevazioni: 
                if(max==valore): #trovo in che mesi si è verificato il valore max
                    mesiMax.append(mese)
                if(min==valore): #trovo in che mesi si è verificato il valore min
                    mesiMin.append(mese)

        
    if(somma==0): #se la somma è uguale a 0 la citta non esiste, quindi nemmeno la tupla
        return "La tupla non esiste!"  
    else: #se la tupla esiste ritorna una tupla con (media, (valoreMax, mesiMax), (valoreMin, mesiMin))
        return (somma/len(rilevazioni), (max, mesiMax), (min, mesiMin))                
     
nomeCitta=input("Inserisci la citta da controllare: ")

#richiamo la funzione per famri stampare la tupla
print(datiPrecipitazioni(nomeCitta))
