import random

# TODO DA RIFARE LA CLASSE ACTOR. FA SCHIFO.
# ________________________________________________________________________________________
class Actor:
    def __init__(self, dir, posX, posY, type):
        self.posX = posX
        self.posY = posY
        self.type = type
        self.dir = dir

    def getType(self):
        return self.type

    def setPos(self, x, y):
        self.posX = x
        self.posY = y

    def act(self):
        pass

#________________________________________________________________________________________
class Tree(Actor):
    def __init__(self, dir, posX, posY, type, treeT=0):
        self.type = "TREE"
        Actor.__init__(self, dir, posX, posY, self.type)

        self.treeTag = treeT
        self.age = 0
        self.food = random.randint(80, 120)  # BOH

    def getType(self):
        return self.type


    def sprawl(self):  #oribbbile da rifare tutta

        p = random.randint(0, 40)
        if p == 1:
            vicini = self.dir.getNeighb(self.posX, self.posY)
            q = random.randint(0, abs(len(vicini) - 1))
            if len(vicini) > 0:
                if vicini[q].getActorList() == []:
                    self.dir.inst(vicini[q].getPos()[0], vicini[q].getPos()[1], "TREE")


    def act(self):
        self.age = self.age + 1
        if (self.age > 12):
            if (self.treeTag == 0):
                self.treeTag = 1
            self.sprawl()
    def getPos(self):
        return self.posX, self.posY

#________________________________________________________________________________________

class Lumberjack(Actor):
    def __init__(self, dir, posX, posY, type):
        Actor.__init__(self, dir, posX, posY, type)
        self.type = "LUMB"
        self.i = True

    def act(self):


        samePosActs = self.dir.getActList(self.posX, self.posY)

        if self.i:
            for i in samePosActs:
                if i.getType() == "TREE":
                    self.dir.removeX(i)
                    self.i = True

        nei = self.dir.getNeighb(self.posX, self.posY)
        i = random.randint(0, abs(len(nei) -1))
        if len(nei) > 0:
            self.dir.moveCel(self, nei[i])


    def getType(self):
        return self.type

    def getPos(self):
        return self.posX, self.posY

#________________________________________________________________________________________

class Bear(Actor):
    def __init__(self):
        self.type = "BEAR"