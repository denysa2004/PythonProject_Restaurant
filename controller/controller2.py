class Controller1:
    def __init__(self,repo):
        self.repo=repo

    def sortGerichte(self):
        return sorted(self.repo.gerichte)

    def addGerichte(self,gericht):
        self.repo.add(gericht)

    def deleteGerichte(self,id):
        self.repo.delete(id)

    def findGerichte(self,id):
        self.repo.find(id)


