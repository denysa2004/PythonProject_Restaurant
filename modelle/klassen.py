from functools import reduce
class Identifizierbar:
    def __init__(self,id):   #die Klasse Identifizierbar als Eltern
        self.id=id


class Kunde(Identifizierbar):  #class Kunde erbt von Identifizierbar
    def __init__(self,id,name,adresse):
        super().__init__(id)
        self.name=name
        self.adresse=adresse


    def __lt__(self, other):
        return self.id < other.id   #die Methode nachdem sie sortiert sind

    def __str__(self):
        return f"Id:{self.id},name:{self.name},adresse:{self.adresse}"
        #die Daten des KUndes
class Gericht(Identifizierbar):   #es erbt auch von Identifizierbar
    def __init__(self, id, name, portionsgrosse, preis):
        super().__init__(id)
        self.portionsgrosse = portionsgrosse
        self.preis = preis
        self.name = name


class Gekochtergericht(Gericht): #erbt von Gericht
    def __init__(self,id,name,portionsgrosse,preis,zeit):
        super().__init__(id,name,portionsgrosse,preis)
        self.zeit = zeit

    def __lt__(self, other):
        return self.id < other.id   #wie sie sortiert sind

    def __str__(self):
        return f"Id:{self.id},name:{self.name},portionsgrosse:{self.portionsgrosse},preis:{self.preis},zeit:{self.zeit}"
    #die Daten des Gerichtes
class Getrank(Gericht):#erbt auch von Gericht
    def __init__(self,id,name,portionsgrosse,preis,alkoohlgehalt):
        super().__init__(id,name,portionsgrosse,preis)
        self.alkoohlgehalt=alkoohlgehalt

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return f"Id:{self.id},name:{self.name},portionsgrosse:{self.portionsgrosse},preis:{self.preis},alkoohlgehalt:{self.alkoohlgehalt}"

    #die Daten des Getranke
class Bestellung(Identifizierbar): #erbt von Identifizierbar
    def __init__(self,k_id,gerichte_ids,getranke_ids):
        super().__init__(k_id)
        self.gerichte_ids=gerichte_ids  #eine liste mit den Ids des bestellten Speisen
        self.getranke_ids=getranke_ids  #liste mit Getranke
        self.gesamtkosten=0.0    #das gesamtkosten

    def kunden_daten(self,k_id,kunden): #wer hat die bestellung gemacht
        for obj in kunden:  #alle objekten von der Kunde
            if obj.id == k_id: #wir sehen ob das Id derselbe ist
                return f"Der Kunde {obj.name} ,mit der Adresse {obj.adresse} hat folgendes bestellt: "

    def bestellten_speisen(self,gerichte,getranke):
        gerichte_name=[]
        getranke_name=[]
        for obj in gerichte:
            if obj.id in self.gerichte_ids:
                 gerichte_name.append(obj.name)   #wir machen eine liste mit den bestellten gerichte

        for obj in getranke:
            if obj.id in self.getranke_ids:
                 getranke_name.append(obj.name) #wir machen eine liste mit den bestellten getranke
        return gerichte_name+getranke_name


    def kosten(self,gerichte,getranke):
        gerichte_preis=[]
        getranke_preis=[]
        for obj in gerichte:
            if obj.id in self.gerichte_ids:
                 gerichte_preis.append(obj.preis)  #eine liste mit den Preis

        for obj in getranke:
            if obj.id in self.getranke_ids:
                 getranke_preis.append(obj.preis)   #eine liste mit den preis

        self.gesamtkosten=reduce(lambda x,y :x+y ,gerichte_preis+getranke_preis,0)
        return f"Die Gesamtkostten ist {self.gesamtkosten} Euro"
    #wir machen den Gesamtkosten von der Liste der Getranke und Liste der Gerichte

    def zeit(self,gerichte):
        gerichte_zeit=[]
        for obj in gerichte:
            if obj.id in self.gerichte_ids:
                 gerichte_zeit.append(obj.zeit) #wir berechnen die Zeit des Bestellungs
        self.gesamtzeit=sum(gerichte_zeit)
        return f"Die Bestellung dauert {self.gesamtzeit} Minuten"

    def afis(self,k_id,kunden,gerichte,getranke):    #das ist die Methode fur alle Daten
        info_kunde=self.kunden_daten(k_id,kunden)
        info_speisen = self.bestellten_speisen(gerichte, getranke)
        info_kosten = self.kosten(gerichte, getranke)
        info_zeit = self.zeit(gerichte)

        return f"{info_kunde}\nBestellte Speisen: {', '.join(info_speisen)}\n{info_kosten}\n{info_zeit}"


