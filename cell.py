import math,actors

class Cell:
    def __init__(self,posX,posY):
        self.x=posX
        self.y=posY
        self.Actor=[]

    def addActor(self,actor):
        self.Actor.append(actor)
