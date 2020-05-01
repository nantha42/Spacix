import pygame as py
import numpy as np

class Explosion(py.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos = np.array([pos[0],pos[1]],int)
        self.rootdir = "img/exp/"
        self.image = None
        self.rect = None
        self.frameindex = -1

    def update(self,player):
        if self.frameindex == 10:
            self.kill()
        self.frameindex+=1
        self.image = py.image.load(self.rootdir+str(self.frameindex)+'.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] - (player.pos[0]) + 520
        self.rect.y = self.pos[1] - (player.pos[1]) + 520
        self.rect.x -= 16
        self.rect.y -= 16