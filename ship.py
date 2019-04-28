import pygame as py 
import numpy as np 
from config import *

import copy

class Player(py.sprite.Sprite):

	def __init__(self,pos,*groups):
		super(Player,self).__init__(*groups)
		self.src = ['img/herohor.png','img/herover1.png']
		self.thrsrc = [['img/thrust1inv.png','img/thrust2inv.png'],['img/thrust1.png','img/thrust2.png']]
		self.inverted = True
		self.thr1img = py.image.load(self.thrsrc[1][0])
		self.thr2img = py.image.load(self.thrsrc[1][1])
		self.landed = False
		self.stopgravity = False
		self.accelerating = False
		self.force = np.array([0.0,0.0])
		self.mass = 100
		self.autorotate = False
		self.missilecount = 0
		self.fuel = 200
		self.requireorbitalvel = 0
		####################

		self.angle = 0
		self.pos = np.array(pos, dtype='float64')
		print(self.pos)
		# self.pos[1] -= 2100
		self.angu_vel = 0
		self.vel = np.array([0.0, 0.0])
		self.accel = np.array([0.0, 0.0])
		self.dt = dt
		self.groundcheck = False
		#####################
		self.image = None
		self.rect = None
		self.invert()


	def invert(self):

		self.inverted = not self.inverted
		if self.inverted:
			self.permimage = py.image.load(self.src[1])
		else: 
			self.permimage = py.image.load(self.src[0])
		self.permimage = py.transform.scale(self.permimage,(30,30));
		self.rect = self.permimage.get_rect()
		self.image = self.permimage
		self.rot_center()

	def nonfireimage(self):
		if self.inverted:
			self.permimage = py.image.load(self.src[1])
		else:
			self.permimage = py.image.load(self.src[0])
		self.permimage = py.transform.scale(self.permimage,(30,30));
		self.rect = self.permimage.get_rect()
		self.image = self.permimage
		self.rot_center()
	
	def accelerate(self):
		#print("accelerating")

		if self.fuel > 0.0:
			self.landed = False
			rad = (self.angle+90)*np.pi/180
			self.accel = playeracceleration*np.array([np.cos(rad),-np.sin(rad)])
			self.stopgravity = False
			self.landed = False
			self.fuel -= 0.1;
			#print(self.angle,self.accel)

			if self.inverted:
				self.permimage = py.image.load(self.thrsrc[1][np.random.randint(0,2)])
			else:
				self.permimage = py.image.load(self.thrsrc[0][np.random.randint(0,2)])
			self.permimage = py.transform.scale(self.permimage, (30, 30));
			self.rect = self.permimage.get_rect()
			self.image = self.permimage
			self.rot_center()


	def decelerate(self):
		self.accelerating = False
		self.vel = np.array([0.0,0.0])
		pass

	def stopaccelerate(self):
		self.accel = np.array([0.0,0.0])

	def rotate(self,clockwise=True):
		if self.inverted:
			if clockwise:
				self.angu_vel -= ship_angular_acceleration
			else:
				self.angu_vel += ship_angular_acceleration
		else:
			if clockwise:
				self.angu_vel -= ship_angular_acceleration
			else:
				self.angu_vel += ship_angular_acceleration

	def setvelocity(self,v):
		rad = (self.angle+90)*np.pi/180
		self.vel = v*np.array([np.cos(rad),-np.sin(rad)])
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

	def update(self,planets):
		self.mask = py.mask.from_surface(self.image)
		checkcoll = False
		for i in planets:
			coll = py.sprite.collide_mask(i,self)

			if coll != None:
				if self.accelerating == False and self.landed == False:
					self.landed = True
					self.groundcheck = True
					checkcoll = True
				else:
					self.landed = True
					self.angu_vel = 0
					pass
				break

		if self.landed == True:
			#self.stopaccelerate()
			self.decelerate()
			self.stopgravity = True
			self.landed = False

		if checkcoll == False:
			self.stopgravity = False
			self.landed = False

		#print(self.vel)
		self.vel = self.vel + self.accel * self.dt
		if checkcoll == False:
			self.pos += self.vel*dt
		self.angle += self.angu_vel
		self.rot_center()
		#print("Two    "+str(self.vel))