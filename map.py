import pygame,math,cell


class Map:
    def __init__(self,dimX,dimY):
        self.dimX = dimX
        self.dimY = dimY
        self.dList = [cell.Cell(x,y) for x in range(self.dimX) for y in range(self.dimY)]
