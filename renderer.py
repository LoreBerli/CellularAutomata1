import pygame

class Renderer:
    def __init__(self, mappa,master):
        self.mappa=mappa
        self.master = master
        pygame.init()
        self.surf = pygame.display.set_mode((712,512),0,32)
        self.rectSide = 8

    def colorOption(self, actorList):

        if len(actorList)==0:
            return (51,25,10)

        if len(actorList)>1:
            return (128,51,0)

        else:

            if actorList[0].getType()== "TREE":

                return (51,102,0)
            if actorList[0].getType()== "LUMB":
                return (204,0,0)
            if actorList[0].getType()== "BEAR":
                return (153,76,0)
            else:
                return (255,255,255)
        #return (255,255,255)

    def drawStats(self):
        alberi = self.master.getNumAttori()[0]
        taglia = self.master.getNumAttori()[1]
        tot = alberi + taglia
        pygame.draw.line(self.surf,(0,0,0),(540,0),(540 ,710),4)
        pygame.draw.line(self.surf,(0,0,0),(544,0),(544 ,710),4)
        pygame.draw.line(self.surf,(51,102,0),(540,710),(540, 710-((alberi*710)/tot)),4)

        pygame.draw.line(self.surf,(204,0,0),(544,0), (544 ,((taglia*710)/tot)),4)


    def draw(self):
        for i in xrange(0,self.mappa.getSize()[0]):
            for j in xrange(0,self.mappa.getSize()[1]):
                color = self.colorOption(self.mappa.getCellActor(i,j))
                pygame.draw.rect(self.surf,color,(i*self.rectSide,j*self.rectSide,self.rectSide,self.rectSide),1)
        pygame.display.update()





