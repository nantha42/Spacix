import pygame as py
import numpy as np
from config import *
import time
class Trail:
    def __init__(self):
        self.points = []
        self.dt = 0
        self.prevtime = time.time()
    def addpoint(self,pos):
        x = pos[0]
        y = pos[1]
        self.points.append([x,y])

    def clear(self):
        self.points.clear()

    def maintainlength(self):
        if len(self.points)>trailmaxlength:
            self.points.pop(0)
            print(len(self.points))

    def draw(self,win,playerpos):
        for i in self.points:
            x = i[0] - (playerpos[0]) + 520
            y = i[1] - (playerpos[1]) + 520
            py.draw.circle(win,(255,255,255),(int(x),int(y)),1,1)

    def autotrail(self,player):
        newtime =time.time()
        if newtime-self.prevtime > 1:
            self.prevtime = newtime
            x = player.pos[0]
            y = player.pos[1]
            self.points.append([x,y])
