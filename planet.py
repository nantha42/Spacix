import numpy as np
import pygame as py
from config import *
import satellite
import clouds
G = 5


class Planet(py.sprite.Sprite):
	def __init__(self,posx,posy,*groups):
		super(Planet,self).__init__(*groups)
		self.mass = planetmass
		self.pos = np.array([posx,posy])
		#print("At planet:",self.pos)
		self.size = size
		self.zoom = 1
		self.radius = self.size*np.sin(np.pi/4)
		self.color=(0,255,0)
		self.image = py.image.load("img/planet.png")
		self.permimage = py.image.load("img/planet.png")
		self.atmos_image = py.image.load("img/atmosphere.png")
		self.permatmos = py.image.load("img/atmosphere.png")
		self.atmos_size = 2300
		self.atmos_rect = self.atmos_image.get_rect()
		self.image = py.transform.scale(self.image,(self.size,self.size))
		self.permimage = py.transform.scale(self.permimage,(self.size,self.size))

		self.rect = self.image.get_rect()
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]
		self.mask = py.mask.from_surface(self.image)
		self.cloud_count = 10
		self.clouds = py.sprite.Group()
		self.old_zoomvalue = 1
		for i in range(self.cloud_count):
			cloud = clouds.Cloud(self.pos,self.radius)
			self.clouds.add(cloud)



	def update(self,cond,pos):
		#cond variable is for walkthrough by arrow keys
		if self.zoom != self.old_zoomvalue:
			self.image = py.transform.scale(self.permimage,(int(self.size*self.zoom),int(self.size*self.zoom)))
			self.rect = self.image.get_rect()
			self.atmos_image = py.transform.scale(self.permatmos,(int(self.atmos_size*self.zoom),int(self.atmos_size*self.zoom)))
			self.atmos_rect = self.atmos_image.get_rect()
			self.mask = py.mask.from_surface(self.image)
			self.old_zoomvalue = self.zoom
		print("Planets",zoom_value)
		print(self.zoom)
		self.rect.centerx = (self.pos[0] - (pos[0]))*self.zoom + 500
		self.rect.centery = (self.pos[1] - (pos[1]))*self.zoom + 500
		self.atmos_rect.centerx = self.rect.centerx
		self.atmos_rect.centery = self.rect.centery
		self.clouds.update(pos)

	def get_satellite(self):
		s = satellite.Satellite()
		s.setvelocity(self)
		return s

class PlanetGenerator:
	def __init__(self):
		self.nplanets = 1
		self.planets = []
		np.random.seed(50344)
		x_list=[x-5 for x in range(10)]
		y_list=[y-5 for y in range(10)]

		for i in range(self.nplanets):
			x = np.random.choice(x_list)
			y = np.random.choice(y_list)
			x_list.remove(x)
			y_list.remove(y)
			p = Planet(x*5500,y*5500);
			self.planets.append(p)

if __name__ == '__main__':
	PG = PlanetGenerator();
