import pygame,math,cell,random,actors


class Map:
    def __init__(self,dimX,dimY):
        self.dimX = dimX
        self.dimY = dimY
        self.dList = [cell.Cell(x,y) for x in xrange(self.dimX) for y in xrange(self.dimY)]

    #def __getattr__(self, x, y):
    #    return self.dList[x*self.dimX + y]

    def getSize(self):
        return [self.dimX, self.dimY]

    def getCellActor(self,x,y):
        return self.dList[x*self.dimX + y].getActorList()

    def getCell(self,x,y):
        return self.dList[x*self.dimX + y]

    def setCellActor(self,dir,x,y,type): # TODO ogni actor dovrebbe avere un riferimento a cella
        tipo=None
        if type=="TREE":
            tipo = actors.Tree(dir,x,y,"TREE")
        if type=="LUMB":
            tipo = actors.Lumberjack(dir,x,y,"LUMB")
        if type=="BEAR":
            tipo = actors.Bear()
        self.dList[x*self.dimX + y].addActor(tipo)
        return self.dList[x*self.dimX + y].getActor()