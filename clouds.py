import pygame as py
import numpy as np
import random

class Cloud(py.sprite.Sprite):

    def __init__(self,pos,planet_radius,*groups):
        super(Cloud,self).__init__(*groups)
        self.clouds_name = ["cloud1.png","cloud2.png"]
        self.image_selected = self.clouds_name[random.randint(0,1)]
        self.zoom = 1
        self.old_zoom = 1

        self.rectwidth = 50
        self.rectheight = 50

        self.permimage = py.image.load("img/"+self.image_selected)
        self.permimage = py.transform.scale(self.permimage, (int(self.rectwidth * self.zoom), int(self.rectheight * self.zoom)))
        self.image = py.image.load("img/"+self.image_selected)

        self.rect = self.image.get_rect()
        self.planet_pos = pos
        self.angle = np.random.randint(0,360)
        radian = np.deg2rad(self.angle)
        self.planet_radius = planet_radius
        self.clock_wise = np.random.randint(0,2)
        self.cloud_height = -400
        self.pos = self.planet_pos + np.array([np.cos(radian),np.sin(radian)])*(self.planet_radius+self.cloud_height)


    def update(self,pos):

        if self.clock_wise == 1:
            self.angle += 0.01
        else:
            self.angle -= .01
        # print(self.angle)
        radian = np.deg2rad(self.angle)
        self.pos =  self.planet_pos + np.array([np.cos(radian),np.sin(radian)])*(self.planet_radius+self.cloud_height)
        self.rot_center(pos)
        x = pos
        if(self.zoom != self.old_zoom):
            self.permimage = py.image.load("img/" + self.image_selected)
            self.permimage = py.transform.scale(self.permimage, (int(self.rectwidth * self.zoom), int(self.rectheight * self.zoom)))

        self.rect.centerx = (self.pos[0] - (pos[0]))*self.zoom + 500
        self.rect.centery = (self.pos[1] - (pos[1]))*self.zoom + 500

    def rot_center(self,pos):
        orig_rect = self.permimage.get_rect()
        rot_image = py.transform.rotate(self.permimage, -self.angle - 90)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image = rot_image
        self.rect = self.image.get_rect()
        # print(self.angle,self.pos[0],self.pos[1],pos[0],pos[1],int(np.linalg.norm(self.planet_pos-self.pos)))

