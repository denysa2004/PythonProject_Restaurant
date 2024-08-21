from ui.cosole import Console
from controller.controller1 import Controller
from controller.controller2 import Controller1
from controller.controller3 import Controller2
from repository.kunde_repo import KundeRepo,FileKundeRepo
from repository.gericht_repo import GerichtRepo,FileGerichtRepo
from repository.getrank_repo import GetrankRepo,FileGetrankRepo
def main1():
    aux=-2
    while aux!=4:
        print("""
                 Wahlen Sie was sie mochten :) 
                 1-Kunde bearbeiten 
                 2-Gerichte bearbeiten
                 3-Getranke bearbeiten                 
                 4-Fertig
                 """)
        #das menu
        aux=int(input('Deine Entscheidung= '))
        if aux==1:
            console=Console(Controller(FileKundeRepo('kunden.dat')))
            console.run()   #wir rufen die console fur kunden
        if aux==2:
            console1 = Console(Controller1(FileGerichtRepo('gerichte.dat')))
            console1.run()   #wir rufen die console fur gerichte
        if aux==3:
            console2 = Console(Controller2(FileGetrankRepo('getranke.dat')))
            console2.run()      #wir rufen die console fur getranke
main1()
