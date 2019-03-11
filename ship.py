import pygame as py 
import numpy as np 

class Player(py.sprite.Sprite):

	def __init__(self,pos):
		super().__init__()
		self.src = ['img/herohor.png','img/herover1.png']
		self.thrsrc = ['img/thrust1.png','img/thrust2.png']
		self.inverted = True;
		self.thr1img = py.image.load(self.thrsrc[0])#for future dev
		self.thr2img = py.image.load(self.thrsrc[1])#for future dev
		self.landed = False;
		self.stopgravity = False
		####################

		self.image = None
		self.rect = None
		self.invert();
		#####################

		self.angle = 0
		self.pos = np.array(pos,dtype='float64')
		self.pos[1] -= 1100
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
		rad = (self.angle+90)*np.pi/180
		self.accel = 10*np.array([np.cos(rad),-np.sin(rad)])
		self.stopgravity = False
		self.landed = False
		#print(self.angle,self.accel)

	def decelerate(self):
		self.vel = np.array([0.0,0.0])
		pass

	def stopaccelerate(self):
		self.accel = np.array([0.0,0.0])

	def update(self):
		#print(self.vel)
		if self.landed == True:
			self.stopaccelerate()
			self.decelerate()
			self.stopgravity = True 
			self.landed = False
		
		temp = self.vel + self.accel*self.dt;
		#print(np.linalg.norm(self.vel))
		self.vel = temp
		#self.vel += -self.accel*self.dt		
		self.pos += self.vel;
		self.angle += self.angu_vel
		self.rot_center();
		#print(self.pos)
		#print("updating")
	
	def rotate(self,clockwise=True):
		if self.inverted:
			if clockwise:
				self.angu_vel = -2
			else:
				self.angu_vel = 2
		else:
			if clockwise:
				self.angu_vel = -2
			else:
				self.angu_vel = 2

	def setvelocity(self,v):
		rad = (self.angle+90)*np.pi/180
		self.vel = v*np.array([np.cos(rad),-np.sin(rad)])*0.1
		#print(self.velocity)

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

	def returnrotcenter(self):
		orig_rect = self.permimage.get_rect()
		
