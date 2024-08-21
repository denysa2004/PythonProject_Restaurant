import pickle
import os
from modelle.klassen import Getrank
class GetrankRepo:
    def __init__(self):
        self.getranke=[]     #eine neue liste fur getranke

    def add(self,getrank):
        self.getranke.append(getrank)    #ein neues getrank hinzufugen

    def find(self,id):
        for getrank in self.getranke:
            if getrank.id == id:       #ein getrank nach dem id suchen
                print(getrank)
    def delete(self,id):
        for getrank in self.getranke:
            if getrank.id == id:              #ein getrank nach dem id loschen
                self.getranke.remove(getrank)
class FileGetrankRepo(GetrankRepo):
    def __init__(self,filename):
        super().__init__()
        self.filename=filename
        self.load()
    def save(self):
        file = open(self.filename, 'ab')  #wir offnen die Datei
        pickle.dump(self.getranke[-1], file)  #es speichert ein neues objekt in den zuvor geoffnete Datei
        file.close()

    def load(self):
        if os.path.exists(self.filename):   #wenn die Datei existiert
            with open(self.filename, 'rb') as file:
                try:
                    while True:
                        loaded_getranke = pickle.load(file)
                        if isinstance(loaded_getranke, Getrank):
                            self.getranke.append(loaded_getranke)  #fugt es ein
                except EOFError:    #ende des Datei
                    pass

    def add(self,getrank):
        super().add(getrank)
        self.save()

