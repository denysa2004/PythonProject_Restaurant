import pickle
import os
from modelle.klassen import Gericht,Gekochtergericht
class GerichtRepo:
    def __init__(self):
        self.gerichte=[]     #eine liste fur gerichte

    def add(self,gericht):
        self.gerichte.append(gericht)      #ein neues gericht hinzufugen

    def find(self,id):
        for gericht in self.gerichte:
            if gericht.id == id:        #das gericht nach dem Id suchen
                print(gericht)
    def delete(self,id):
        for gericht in self.gerichte:
            if gericht.id == id:               #ein gericht nach dem id loschen
                self.gerichte.remove(gericht)
class FileGerichtRepo(GerichtRepo):  #es erbt von GerichtRepo
    def __init__(self,filename):
        super().__init__()
        self.filename=filename
        self.load()
    def save(self):
        file = open(self.filename, 'ab')     #append to the file
        pickle.dump(self.gerichte[-1], file)    #es speichert ein neues objekt in den zuvor geoffnete Datei
        file.close()

    def load(self):
        if os.path.exists(self.filename):  #wenn die Datei existiert
            with open(self.filename, 'rb') as file:  #wir offnen die Datei
                try:
                    while True:
                        loaded_gerichte = pickle.load(file)
                        if isinstance(loaded_gerichte, Gericht): #wenn es das Objekt eine Instant ist dann fugt es sie hinzu
                            self.gerichte.append(loaded_gerichte)
                except EOFError:
                    pass

    def add(self,gericht):
        super().add(gericht)
        self.save()