import pygame as py
import numpy as np
from config import *
class Satellite(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("img/sat.png")
        self.rect = self.image.get_rect()
        self.pos = np.array([0,0],float)
        self.vel = np.array([0,0],float)
        self.belongedplanet = None

    def setvelocity(self,planet):
        self.pos[1] = planet.pos[1]
        print("1",self.pos[1])
        self.pos[0] = planet.pos[0]+1200

        self.belongedplanet = planet
        r = planet.pos-self.pos
        dis = np.linalg.norm(r)
        g = planet.mass/(dis**2)
        g_vec = g*r/dis
        unit = r/dis
        mag = np.sqrt(planet.mass/dis)
        if unit[1] !=0:
            vy = -unit[0]/unit[1]
            unit1 = np.array([unit[0], vy])
        else:
            print("Here",unit)
            unit1 =  np.array([0,1])

        self.vel = unit1*mag

    def update(self,pos):
        r = self.belongedplanet.pos - self.pos
        dis = np.linalg.norm(r)
        g = self.belongedplanet.mass/(dis**2)
        g_vec = g*r/dis
        self.vel += g_vec*dt
        self.pos += self.vel*dt
        print(dis)
        self.rect.x = int(r[0]+self.belongedplanet.rect.x+(2000*np.sin(np.pi/4)))
        self.rect.y = int(r[1] + self.belongedplanet.rect.y + (2000 * np.sin(np.pi / 4)))

    def draw(self,win):
        py.draw.line(win,(255,255,255),[self.rect.x,self.rect.y],[self.belongedplanet.rect.x+(1000*np.sin(np.pi/4)),self.belongedplanet.rect.y+(1000*np.sin(np.pi/4))],10)