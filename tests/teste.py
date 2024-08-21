import unittest
import pickle
import os
from repository.gericht_repo import GerichtRepo
from repository.kunde_repo import KundeRepo
from controller.controller2 import Controller1
from controller.controller1 import Controller
from modelle.klassen import Gekochtergericht,Kunde,Bestellung,Getrank
class Testen(unittest.TestCase):
    def setUp(self):
        self.repo=GerichtRepo()
        self.controller=Controller1(self.repo)
        self.repo1=KundeRepo()
        self.controller1=Controller(self.repo1)
        self.kunde_repo = KundeRepo()
        self.kunde1 = Kunde(1, 'Bob', 'lla')
        self.kunde2 = Kunde(2, 'Dora', 'lalal')
        self.kunde_repo.add(self.kunde1)
        self.kunde_repo.add(self.kunde2)
        self.kunde = [Kunde(1, 'Bob', 'lastrada')]
        self.gerichte = [Gekochtergericht(101, 'Pizza', 2, 10, 25), Gekochtergericht(102, 'Salad', 1, 8, 15)]
        self.getranke = [Getrank(201, 'Cola', 1, 3, 0), Getrank(202, 'Orange Juice', 1, 4, 0)]

    def test_addGericht(self):
        gericht=Gekochtergericht(9,'Spaghetii',2,10,30)
        self.controller.addGerichte(gericht)
        #wir fugen ein neues Gericht hinzu
        added_gericht=self.repo.gerichte[-1]
        #das ist das letzte Gericht
        self.assertEqual(added_gericht,gericht,'Nicht hinzugefugt')


    def test_find_Kunde_Teilnames(self):
        kunde=Kunde(1,'denisa','plopilor')
        self.controller1.addKunden(kunde)
        #wir fugen ein Kunde ein
        teilname='den'
        suche_kunde=self.controller1.findKunden(teilname)
        if suche_kunde is not None:
            self.assertIn(kunde,suche_kunde,'Nicht gefunden')
        else:
            self.fail('findKunden returned None')

    def test_find_Kunde_Teiladresse(self):
        kunde=Kunde(1,'denisa','plopilor')
        self.controller1.addKunden(kunde)
        #wir fugen ein Kunde ein
        teiladresse='plop'
        suche_kunde=self.controller1.findKunden(teiladresse)
        if suche_kunde is not None:
            self.assertIn(kunde,suche_kunde,'Nicht gefunden')
        else:
            self.fail('findKunden returned None')

    def test_updateKundenName(self):
        kunden_id = 1
        new_name = 'Dob'
        #neues Name
        self.kunde_repo.updateKundenName(kunden_id, new_name)
        updated_kunde = None
        for kunde in self.kunde_repo.kunden:
            if kunde.id == kunden_id:  #wir durchgehen alle Kunde von der Liste
                updated_kunde = kunde
                break
        self.assertIsNotNone(updated_kunde)  #wenn wir der Kunde finden
        self.assertEqual(updated_kunde.name, new_name, 'Name was not updated')

    def test_kosten(self):
        bestellung = Bestellung(1, [101, 102], [201, 202])
        gesamtkosten = bestellung.kosten(self.gerichte, self.getranke)
        self.assertEqual(gesamtkosten, "Die Gesamtkostten ist 25 Euro")

    def test_afis(self):
        bestellung = Bestellung(1, [101, 102], [201, 202])
        result = bestellung.afis(1, self.kunde, self.gerichte, self.getranke)
        expected_result = "Der Kunde Bob ,mit der Adresse lastrada hat folgendes bestellt: \nBestellte Speisen: Pizza, Salad, Cola, Orange Juice\nDie Gesamtkostten ist 25 Euro\nDie Bestellung dauert 40 Minuten"
        self.assertEqual(result, expected_result)

    def test_save_bestellung_to_file(self):
        test_bestellung = Bestellung(1, [1, 2], [3, 4])
        test_filename = 'test_bestellung_save.dat'  # in einer Detei speichern
        with open(test_filename, 'wb') as file:
            pickle.dump(test_bestellung, file)
        self.assertTrue(os.path.exists(test_filename))  # wir prufen ob die Datei nach dem Speichern existiert
        os.remove(test_filename)  # wir loschen die erstellte Datei

    def test_load_bestellung_from_file(self):
        test_bestellung = Bestellung(2, [5, 6], [7, 8])
        test_filename = 'test_bestellung_load.dat'
        with open(test_filename, 'wb') as file:
            pickle.dump(test_bestellung, file)

        with open(test_filename, 'rb') as file:
            loaded_bestellung = pickle.load(file)

        self.assertIsNotNone(loaded_bestellung)

        os.remove(test_filename)#wir loschen die erstellte Datei

if __name__=='__main__':
    unittest.main()