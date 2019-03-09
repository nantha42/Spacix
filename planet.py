import numpy as np
import pygame as py 
G = 5
class Planet(py.sprite.Sprite):
	def __init__(self,pos):
		super().__init__();
		self.mass = 0;
		self.pos = np.array(pos);
		self.radius = 1000
		self.color=(0,255,0)
		self.image = py.Surface((self.radius*2,self.radius*2)) 
		self.create(self.color);
		self.rect = self.image.get_rect();
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]

	def create(self,color):
		py.draw.circle(self.image,color,(self.radius,self.radius),self.radius,self.radius);
		self.mask = py.mask.from_surface(self.image);

	def update(self,pos):
		self.rect.x-=pos[0]
		self.rect.y-=pos[1]

class PlanetGenerator:
	def __init__(self):
		self.nplanets = 10
		self.planets = []
		np.random.seed(50344)
		x_list=[x-5 for x in range(10)]
		y_list=[y-5 for y in range(10)]

		print(x_list,y_list)
		
		for i in range(self.nplanets):
			x = np.random.choice(x_list)
			y = np.random.choice(y_list)
			x_list.remove(x)
			y_list.remove(y)
			p = Planet((x*5500,y*5500));
			self.planets.append(p)
		

if __name__ == '__main__':
	PG = PlanetGenerator();
	for i in PG.planets:
		print(i.pos,i.radius)


