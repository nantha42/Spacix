import numpy as np
import pygame as py
class Bar:
    def __init__(self):
        pass

    def draw(self,win,val,fullval):
        len = val*200/fullval
        py.draw.rect(win,(int(255-2.55*val/2),int(2.55*val/2),0),(10,10,len,10))
        #/Users/nantha/Projc/my_projects/Spacic/scores