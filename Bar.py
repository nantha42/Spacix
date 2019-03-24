import numpy as np
import pygame as py
class Bar:
    def __init__(self):
        pass

    def draw(self,win,val,fullval):
        len = val*200/fullval
        py.draw.rect(win,(0,255,0),(10,10,len,10))