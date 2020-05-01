import pygame as py;
import numpy as np;
class Map(py.sprite.Sprite):
	def __init__(self,planets):
		super().__init__();
		self.planets = planets;
		self.size = (210,210)
		self.image = py.Surface(self.size);
		self.image.set_colorkey((0,0,0))
		self.tempimage=None;
		self.offset = [12,12]
		self.planetcolor = (200,55,20)
		py.draw.line(self.image,(100,100,100),(10,0),(10,self.size[1]),4)
		for i in self.planets:
			p = np.array(i.pos/2750,dtype=int);
			#print(p)
			p += self.offset
			py.draw.circle(self.image,self.planetcolor,p*10,2,2);
		self.tempimage = list([self.image])
		self.rect = self.image.get_rect();
		self.set_rect();
	def set_rect(self):
		self.rect.x = 900-210;
		self.rect.y = 10;

	def update(self,playerpos):
		self.image = py.Surface(self.size);
		self.image.set_colorkey((0,0,0))
		py.draw.line(self.image,(100,100,100),(5,0),(5,self.size[1]-5),4)
		py.draw.line(self.image,(100,100,100),(5,self.size[1]-5),(self.size[0],self.size[1]-5),4)
		self.tempimage=None;
		for i in self.planets:
			p = np.array(i.pos/2750,dtype=int);
			#print(p)
			p += self.offset
			py.draw.circle(self.image,self.planetcolor,p*10,1,1);
		
		p = np.array(playerpos/2750,dtype=int);
		p += self.offset;
		py.draw.circle(self.image,(255,255,255),p*10,2,2);
		
