import os
import pickle
from modelle.klassen import Kunde
class KundeRepo:
    def __init__(self):
        self.kunden=[]           #eine liste fur kunden

    def add(self,kunde):
        self.kunden.append(kunde)     #ein neue Kunde hinzufugen

    def find(self,suchen):#suchen kann entweder die adresse oder die name sein
        kundenlist=[]
        for kunde in self.kunden:#wir durchgehen alle kunden von der liste
            if suchen.lower() in kunde.name.lower() or suchen.lower() in kunde.adresse.lower():     #ein kunde nach dem name name und adresse suchen
                kundenlist.append(kunde)
        return kundenlist
    def delete(self,id):
        for kunde in self.kunden:
            if kunde.id == id:                #ein kunde nach dem id loschen
                self.kunden.remove(kunde)

    def updateKundenName(self, kunden_id, new_name):
        for kunde in self.kunden:
            if kunde.id == kunden_id:
                kunde.name = new_name
                return True
        return False
class FileKundeRepo(KundeRepo):
    def __init__(self,filename):
        super().__init__()
        self.filename=filename
        self.load()

    def save(self):#wir speichern ein neue Kunde
        file=open(self.filename,'ab')  #append
        pickle.dump(self.kunden[-1],file) #der letzte Kunde
        file.close()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename,'rb') as file: #wir offnen die Datei
                try:
                    while True:
                        loaded_kunde=pickle.load(file)
                        if isinstance(loaded_kunde, Kunde):

                            self.kunden.append(loaded_kunde)
                except EOFError:  #ende des Datei
                    pass
    def add(self,kunde):
        super().add(kunde)
        self.save()