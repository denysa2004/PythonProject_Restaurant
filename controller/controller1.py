class Controller:             #class controller fur kunde
    def __init__(self,repo):
        self.repo=repo

    def sortKunden(self):
        return sorted(self.repo.kunden)    #die funktion fur ordnung der Kunden

    def addKunden(self,kunde):
        self.repo.add(kunde)     #die Funktion fur einen neuen Kunde hinzufugen

    def deleteKunden(self,id):
        self.repo.delete(id)      #die Funktion fur loschen des Kundes

    def findKunden(self,suchen):
        return self.repo.find(suchen)     #die funktion fur suchen den Kunde

    def updateKundenName(self, kunden_id, new_name):
        return self.repo.updateKundenName(kunden_id, new_name)  #die funktion fur aktualisierung des Kundes
