import numpy as np
import pygame as py
from config import *
G = 5

class Planet(py.sprite.Sprite):
	def __init__(self,posx,posy,*groups):
		super(Planet,self).__init__(*groups);
		self.mass = planetmass
		self.pos = np.array([posx,posy]);
		print("At planet:",self.pos)
		self.radius = 1000
		self.color=(0,255,0)

		self.image = py.image.load("img/planet.png")
		self.rect = self.image.get_rect();
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]
		self.mask = py.mask.from_surface(self.image)

	def create(self,color):
		py.draw.circle(self.image,color,(self.radius,self.radius),self.radius,self.radius);
		self.mask = py.mask.from_surface(self.image);

	def update(self,cond,pos):
		#cond variable is for walkthrough by arrow keys
		if cond == 1:
			self.rect.x-=(pos[0]+10)
			self.rect.y-=(pos[1]+10)

		elif cond == 2:
			self.rect.x = self.pos[0]-(pos[0]) - 1000*np.sin(np.pi/4) + 250
			self.rect.y = self.pos[1]-(pos[1]) - 1000*np.sin(np.pi/4) + 250
			#self.rect.x = self.pos[0]-(pos[0]) - 1000
			#self.rect.y = self.pos[1] -(pos[1]) - 1000


class PlanetGenerator:
	def __init__(self):
		self.nplanets = 10
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
	for i in PG.planets:
		print(i.pos,i.radius)


