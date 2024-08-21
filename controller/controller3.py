class Controller2:
    def __init__(self,repo):
        self.repo=repo

    def sortGetranke(self):
        return sorted(self.repo.getranke)

    def addGetranke(self,getrank):
        self.repo.add(getrank)

    def deleteGetranke(self,id):
        self.repo.delete(id)

    def findGetranke(self,id):
        self.repo.find(id)


