import math,actors

class Cell:
    def __init__(self,posX,posY):
        self.x=posX
        self.y=posY
        self.Actor=[]

    def addActor(self,actor):
        self.Actor.insert(0,actor)

    def rmvActor(self,actor):
        self.Actor.remove(actor)

    def getPos(self):
        return  [self.x,self.y]

    def getActor(self):
        if len(self.Actor)>0:
            return self.Actor[0]
        else:
            return

    def getActorList(self):
        return  self.Actor