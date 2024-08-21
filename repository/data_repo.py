import pickle
class DataRepo:
    def _init_(self, datei):
        self.datei = datei

    def read_file(self):
        try:
            with open(self.datei, 'rb') as file:    #die Datei lesen
                return file.read()
        except FileNotFoundError:
            return b''

    def write_to_file(self, daten_string):
        with open(self.datei, 'wb') as file:   #in Datei etwas neues zu schreiben
            file.write(daten_string)
    def convert_to_string(self, objekte):
        return pickle.dumps(objekte)           #er speichert alle objekten in den Datei

    def convert_from_string(self, daten_string):   #er nimmt alle objekten von den Datei
        return pickle.loads(daten_string)
    import pickle
