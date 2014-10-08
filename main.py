import actors
import director
import renderer
import map

import time

mappa = map.Map(64,64)
#mappa.dummyRandomPopulate()
rend = renderer.Renderer(mappa)
master = director.gameDirector(mappa)
master.start()

rend.draw()

while master.getTick()<400:

    master.tick()
    rend.draw()

