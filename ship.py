import pygame as py 
import numpy as np 

class Player(py.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.src = ['img/herohor.png','img/herohor1.png']
		self.inverted = True;
		
		####################
		self.image = None
		self.rect = None
		self.invert();
		#####################
		self.angle = 0
		self.pos = np.array([0.0,0.0])
		self.angu_vel = 0;
		self.vel = np.array([0.0,0.0])
		self.accel = np.array([0.0,0.0])
		self.dt = 0.01;

	def invert(self):
		self.inverted = not self.inverted;
		if self.inverted:
			self.permimage = py.image.load(self.src[1])
		else: 
			self.permimage = py.image.load(self.src[0])
		self.rect = self.permimage.get_rect()
		self.image = self.permimage;
	
	def accelerate(self):
		rad = self.angle*np.pi/180
		self.accel = 10*np.array([np.cos(rad),np.sin(rad)])

	def update(self):
		self.vel += self.accel*self.dt;
		self.pos += self.vel*self.dt;
		self.angle += self.angu_vel
		self.rot_center();
		print("updating")
	
	def rotate(self,clockwise=True):
		if self.inverted:
			if clockwise:
				self.angu_vel = 5
			else:
				self.angu_vel = -5
		else:
			if clockwise:
				self.angu_vel = -5
			else:
				self.angu_vel = 5
	def stoprotate(self):
		self.angu_vel = 0;

	def rot_center(self):
		orig_rect = self.permimage.get_rect()
		rot_image = py.transform.rotate(self.permimage, self.angle-90)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		self.image = rot_image
		self.rect = self.image.get_rect()
		self.rect.x = 500
		self.rect.y = 500

