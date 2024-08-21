import pickle
from modelle.klassen import Bestellung,Kunde,Getrank,Gekochtergericht,Gericht

def load_objects_from_pickle(filename='gerichte.dat'):
    try:
        with open(filename, 'rb') as file:    #wir offnen das Datei
            objects = []
            while True:                            #alle objekte von gerichte
                gerichte = pickle.load(file)
                objects.append(gerichte)
    except EOFError:  #das Ende des File
        return objects
def load_objects_from_pickle1(filename='getranke.dat'):
    try:
        with open(filename, 'rb') as file:
            objects = []
            while True:                               #alle objekte von getranke
                getranke = pickle.load(file)
                objects.append(getranke)
    except EOFError:
        return objects
def load_objects_from_pickle2(filename='kunden.dat'):
    try:
        with open(filename, 'rb') as file:
            objects = []                                 #alle objekte von kunden
            while True:
                kunde = pickle.load(file)
                objects.append(kunde)
    except EOFError:
        return objects
def menu():
    return """
           Wilkomnen zu unserer Restaurant!!!
           Bitte Drucken sie :
           1-Gerichte sehen
           2-Getranke sehen
           3-Bestellung machen
           4-Fertig
     """

def bestellung():
    print(menu())
    entscheidung=-1
    while entscheidung!=0:
        entscheidung=int(input('Deine Entscheidung= '))
        if entscheidung==1:
            with open('gerichte.dat', 'rb') as file:  #wir offnen das Datei
                try:
                    while True:
                        data1 = pickle.load(file)  #wir nehmen alle Daten von pickle gerichte
                        print(data1)
                except EOFError:            #wenn wir fertig sind
                    pass                    #wir geben das menu mit den gerichten
        if entscheidung==2:
            with open('getranke.dat', 'rb') as file:
                try:
                    while True:
                        data2 = pickle.load(file)
                        print(data2)             #wir geben die getranke
                except EOFError:          #wenn wir fertig sind
                    pass
        if entscheidung==3:
            print('Bitte drucken Sie 0000 , um Sie in unserer Restaurantbasis zu finden')
            id_k=int(input("Drucken= "))
            if id_k==0000:
                from app.main import main1
                id_k = int(input("id Kunde= "))
            gerichte_ids = []   #eine liste mit ids fur bestellten gerichte
            getranke_ids = []   #eine liste mit ids fur bestellten getranke
            id_gericht = -1
            id_getrank = -1
            print("Bitte geben Sie alle Ids den Gerichten ,welche Sie bestellen mochten ,0-wenn sie fertig sind")
            while id_gericht != 0:
                id_gericht = int(input('id_gericht= '))
                if id_gericht != 0:
                    gerichte_ids.append(id_gericht)    #wir tuen alle ids die bestellt sind
            print("Bitte geben Sie alle Ids den Getranken ,welche Sie bestellen mochten ,0-wenn sie fertig sind")
            while id_getrank != 0:
                id_getrank = int(input('id_getranke= '))
                if id_getrank != 0:
                    getranke_ids.append(id_getrank)    #wir tuen alle ids die bestellt sind fur getranke
            gerichten = load_objects_from_pickle()    #alle objekten von gerichte
            getranken = load_objects_from_pickle1()   #alle objekten von getranke
            kunde = load_objects_from_pickle2()       #alle objekten von kunden
            bestellung = Bestellung(id_k, gerichte_ids, getranke_ids) #das neue objekt von bestellung
            bestellung.kunden_daten(id_k, kunde) #die methode von bestellung
            bestellung.bestellten_speisen(gerichten, getranken)  #die liste mit den bestellten speisen
            bestellung.kosten(gerichten, getranken) #das kosten des bestellungs
            bestellung.zeit(gerichten)  #die methode fur die zeit des bestellungs
            print(bestellung.afis(id_k, kunde, gerichten, getranken))
                   #wir geben das Rechnung mit allen Daten
        if entscheidung == 4:
            break

bestellung()