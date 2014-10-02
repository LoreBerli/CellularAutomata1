import math,actors

class Cell:
    def __init__(self,posX,posY):
        self.x=posX
        self.y=posY
        self.Actor=None

    def setActor(self,actor):
        self.Actor=actor
