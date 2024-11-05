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
                #print(mese)
                #print(valore)
                somma+=valore
                if(valore>max):
                    max=valore
                if(valore<min):
                    min=valore
            for mese, valore in rilevazioni: 
                if(max==valore):
                    mesiMax.append(mese)
                if(min==valore):
                    mesiMin.append(mese)

        
    if(somma==0):
        return "La tupla non esiste!"  
    else: 
        return (somma/len(rilevazioni), (max, mesiMax), (min, mesiMin))                
        #print(somma/len(rilevazioni)) 
        #print("Max ", max)
        #print("Min ", min) 
        #print("Mese/i min: ", mesiMin)
        #print("Mese/i max: ", mesiMax)
     
    
nomeCitta=input("Inserisci la citta da controllare: ")
       
print(datiPrecipitazioni(nomeCitta))