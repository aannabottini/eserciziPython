class Macchina:
    def __init__(self, targa, marca, modello, anno):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def __str__(self):
        # Restituisce una descrizione leggibile della macchina
        return f"{self.marca} {self.modello} ({self.anno}) - Targa: {self.targa}"

class Garage:
    def __init__(self):
        # Inizializza la lista delle macchine
        self.listaMacchine = []

    def aggiungi_macchina(self, macchina):
        # Aggiunge una macchina alla lista
        i = 0
        for macchinaFor in self.listaMacchine:
            if(macchinaFor.targa==macchina.targa):
                print("Macchina già presente")
                i+=1
        if(i==0):
            self.listaMacchine.append(macchina)
            

    
    def rimuovi_macchina(self, targa):
        # Rimuove una macchina in base alla targa
        i = 0
        for macchinaFor in self.listaMacchine:
            if(macchinaFor.targa==targa):
                self.listaMacchine.remove(macchinaFor)
                print("Macchina rimossa correttamente")
                i+=1
        if(i==0):
            print(f"Non esiste la macchina")

    def elenco_macchine(self):
        # Mostra tutte le macchine nel garage
        i = 0
        print("Macchine presenti nel garage: ")
        for macchina in self.listaMacchine:
            print(macchina)
            i+=1
        if(i==0):
            print("Garage vuoto!")

    def cerca_macchina(self, targa):
        # Cerca e restituisce le informazioni di una macchina tramite la targa
        i = 0
        for macchina in self.listaMacchine:
            if(macchina.targa==targa):
                print(macchina)
                i+=1
        if(i==0):
            print("Macchina non presente")

macchina = Macchina ("AA123BB", "Marca", "Modello", 1990)
macchina2 = Macchina ("BB123BB", "Marca1", "Modello1", 2001)

garage = Garage()
garage.aggiungi_macchina(macchina)
garage.aggiungi_macchina(macchina2)

garage.elenco_macchine()

print("\nRicerca della macchina: ")
garage.cerca_macchina("AA123BB")

print("\nRimozione della macchina: ")
garage.rimuovi_macchina("AB123BB")
