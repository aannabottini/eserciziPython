import math

class Pagella:


    def __init__(self, pagella):
        self.pagella = pagella
    
    def __str__(self):
        stringa = ""
        for i in range(len(self.pagella)):
            stringa+=f"{self.pagella[i]}\n"
        return stringa

    def media(self):
        media = 0
        i = 0
        for voto in self.pagella:
            media+=voto
            i+=1
        return media/i
    
    def __getitem__(self, index):
        if(len(self.pagella)<index):
            return "Indice non valido"
        for i in range(len(self.pagella)):
            if(i==index):
                return self.pagella[i]
    
    def __eq__(self, voti):
        if(len(self.pagella)<=0):
            return "Impossibile comparare due Pagelle"
        for i in range(len(self.pagella)):
            if(self.pagella[i]==voti[i]):
                uguali = True
            else: 
                uguali = False
        return uguali
    
    def __sub__(self, voti):
        if(len(self.pagella)<=0):
            return "Impossibile effettuare la sottrazione"
        array = []
        for i in range(len(self.pagella)):
            array.append(self.pagella[i]-voti[i])
        nuovaPagella = Pagella(array)
        return nuovaPagella
         
    def impegno(self):
        impegno = 0
        for i in range(len(self.pagella)):
            impegno+=self.pagella[i]*self.pagella[i]
        return math.sqrt(impegno)
    
pagella = Pagella([6,7,8])
pagella1 = Pagella([6,7,8])
while(True):
    print("1. Visualizza lista voti;")
    print("2. Media voti pagella;")
    print("3. Visualizza il voto all'indice i;")
    print("4. Confronta due oggetti pagella;")
    print("5. Sottrae due pagelle;")
    print("6. Impegno.")
    print("7. Esci")
    scelta = int(input("scelta: "))
    if(scelta>=7):
        break

    if(scelta==1):
        print("Stampo pagella: ")
        print(pagella)

    if(scelta==2):
        print("Media voti pagella: ")
        print(pagella.media())
    
    if(scelta==3):
        while(True):
            i = int(input("inserisci indice: "))
            if(i>=0):
                break
        print(pagella[i])

    if(scelta==4):
        if(pagella.__eq__(pagella1)):
            print("Pagelle uguali")
        else: 
            print("Pagelle diverse")
    
    if(scelta==5):
        print(pagella.__sub__(pagella1)) #0, 0, 0

    if(scelta==6):
        print(pagella.impegno())












