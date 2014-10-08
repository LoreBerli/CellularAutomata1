import actors
import director
import renderer
import map
import pygame
import sys

import time

mappa = map.Map(64,64)
#mappa.dummyRandomPopulate()

master = director.gameDirector(mappa)
rend = renderer.Renderer(mappa,master)
master.start()
fpsClock = pygame.time.Clock()
rend.draw()

while master.getTick()<400:

    master.tick()
    rend.draw()
    rend.drawStats()
    fpsClock.tick(30)

