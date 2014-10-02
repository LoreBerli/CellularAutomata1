import random

class Actor:
    def __init__(self,posX,posY):
        self.posX=posX
        self.posY=posY

class Tree(Actor):
    def __init__(self):
        self.type = "TREE"
        self.age=0
        self.food = random.randint(80,120)



class LumberJack(Actor):
    def __init__(self):
            self.type = "LUMBERJACK"




class Bear(Actor):
    def __init__(self):
        self.type = "BEAR"