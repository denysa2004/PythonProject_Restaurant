from modelle.klassen import Kunde,Gekochtergericht,Gericht,Getrank

class Console:
    def __init__(self,controller):
        self.controller=controller

    def menu(self):
        return """
        
        1-neue kunde hinzufugen      5-neues gericht hinzufugen     9-neuer Getrank hinzufugen     13-Bestellung machen
        2-alle kunden sehen          6-alle gerichte sehen          10-alle Getranke sehen            
        3-suchen des Kundes          7-suchen die Gerichte         11-suchen den Getrank
        4-loschen des Kundes         8-loschen die Gerichte       12-loschen die Getranke
        13-name akutalisieren
        0-exit von hier
        """

    #das menu
    def run(self):
        while True:
            print(self.menu())
            value=int(input())  #unsere Entscheidung
            if value==0:
                break
            if value==1:
                id=int(input('Id des Kundes: '))
                name=input("name=")
                adresse=input("adresse=")       #ein neue kunde hinzufugen
                kunde=Kunde(id,name,adresse)
                self.controller.addKunden(kunde)

            if value==2:
                kunden=self.controller.sortKunden()
                for kunde in kunden:              #alle kunde sehen
                    print(kunde)

            if value==3:
                suchen=input('Name oder Adresse des Kundes :')
                kunden=self.controller.findKunden(suchen)    #ein kunde suchen
                for kunde in kunden:
                    print(kunde)
            if value==4:
                id = int(input('Id des Kundes: '))
                self.controller.deleteKunden(id)   #ein kunde loschen

            if value==5:
                id=int(input('Id des Gerichtes: '))
                name=input('name=')
                portionsgrosse=int(input("portionsgrosse="))
                preis=int(input("preis="))
                zeit=int(input("zeit="))
                gericht=Gekochtergericht(id,name,portionsgrosse,preis,zeit)
                self.controller.addGerichte(gericht)
                     #ein neues gericht hinzufugen
            if value==6:
                gerichte=self.controller.sortGerichte()
                for gericht in gerichte:
                    print(gericht)
                   #alle gerichte sehen
            if value==7:
                id=int(input('Id des Gerichtes: '))
                self.controller.findGerichte(id)
                #ein gericht nach dem id suchen
            if value==8:
                id = int(input('Id des Gerichtes: '))
                self.controller.deleteGerichte(id)
                #ein gericht loschen

            if value==9:
                id=int(input('Id der Getrank: '))
                name=input('name=')
                portionsgrosse=int(input("portionsgrosse="))
                preis=int(input("preis="))
                alkoohl=int(input('alkoohlgehalt='))
                getrank=Getrank(id,name,portionsgrosse,preis,alkoohl)
                self.controller.addGetranke(getrank)
                #ein neues getrank hinzufugen
            if value==10:
                getranke=self.controller.sortGetranke()
                for getrank in getranke:
                    print(getrank)
                 #die getranke sortieren
            if value==11:
                id=int(input('Id der Getrank: '))
                self.controller.findGetranke(id)
                 #ein getrank suchen
            if value==12:
                id = int(input('Id der Getrank: '))
                self.controller.deleteGetranke(id)

                  #ein getrank loschen
            if value == 13:
                id = int(input('Id des Kundes:'))
                neue_name = input('Neuer Name:')
                updated = self.controller.updateKundenName(id, neue_name)
                if updated:
                    print('Kundenname erfolgreich aktualisiert.')
                else:
                    print('Kunde mit dieser Id nicht gefunden.')

            #name aktualisieren