import random

import map
import cell
import actors


class gameDirector:
    def __init__(self, mappa):
        self.mappa = mappa
        self.attori = []
        self.tagliaL = 0
        self.albe = 0
        self.orsi = []
        self.time = 0
        self.popuLimit = 500

    # def update(self): #Director ha la responsabilita
    def getNumAttori(self):
        return self.albe,self.tagliaL

    def tick(self):
        self.albe=self.tagliaL=0
        if self.time % 12 == 0:
            self.yearPassed()
        x = 0
        self.time = self.time + 1

        for i in xrange(len(self.attori),-1,-1):
            if self.attori[i-1].getType()=="TREE":
                self.albe=self.albe+1
            else : self.tagliaL=self.tagliaL+1

            self.attori[i-1].act()

        x = x + 1

    def getTick(self):
        return self.time

    def getActList(self, x, y):
        return self.mappa.getCell(x, y).getActorList()

    def getNeighb(self, x, y):
        nei = []
        for i in xrange((x - 1) % self.mappa.getSize()[0], (x + 2) % self.mappa.getSize()[0]):
            for j in xrange((y - 1) % self.mappa.getSize()[1], (y + 2) % self.mappa.getSize()[1]):
                if ((x,y)!=(i,j)):
                    nei.append(self.mappa.getCell(i, j))

        return nei

    def inst(self, x, y, typeO):
        if typeO == "TREE":
            self.attori.append(self.mappa.setCellActor(self, x, y, typeO))
        if typeO == "BEAR":
            self.attori.append(self.mappa.setCellActor(self, x, y, typeO))
        if typeO == "LUMB":
            self.attori.append(self.mappa.setCellActor(self, x, y, typeO))

    def yearPassed(self):
        pass

    def removeX(self,actor):
        position = actor.getPos()
        cella = self.mappa.getCell(position[0], position[1])
        cella.rmvActor(actor)
        self.attori.remove(actor)



    def moveCel(self, actor, Cell):
        tipo = actor.getType()
        position = actor.getPos()
        cella = self.mappa.getCell(position[0], position[1])
        cellaNuova = Cell
        cella.rmvActor(actor)
        cellaNuova.addActor(actor)
        actor.setPos(cellaNuova.getPos()[0], cellaNuova.getPos()[1])

    def start(self):
        "populates the map randomly"
        while self.popuLimit > 0:
            for i in xrange(1, self.mappa.getSize()[0]-1):
                for j in xrange(1, self.mappa.getSize()[1]-1):
                    p = random.randint(0, 100)
                    if p <= 62 and self.popuLimit > 0:
                        if p < 2:
                            pass
                            #self.inst(i,j,"BEAR")
                        if p > 2 and p < 8:
                            pass
                            self.inst(i, j, "LUMB")
                            self.popuLimit = self.popuLimit - 1
                        if p >= 10 and p < 16:
                            self.inst(i, j, "TREE")
                            self.popuLimit = self.popuLimit - 1







