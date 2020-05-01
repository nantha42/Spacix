import pygame as py
import numpy as np
from config import *
import time

class Missile(py.sprite.Sprite):
	def __init__(self, ship,name,zoom):
		super().__init__()
		self.permimage = py.image.load("img/pmiss2.png")
		self.rectheight = 6
		self.rectwidth = 6
		self.image = None
		self.rect = None
		self.ships = ship
		self.angle = ship.angle
		self.zoom = zoom
		self.old_zoom = 1
		self.permimage = py.transform.scale(self.permimage, (int(self.rectwidth*self.zoom),int( self.rectheight*self.zoom)))
		self.rot_center()

		rad = (self.angle+90)*np.pi/180
		v = ship.vel
		#self.accel = 100*np.array([np.cos(rad),-np.sin(rad)])
		self.accel = np.array([0.0,0.0])
		self.vel = ship.vel

		self.move = True
		self.pos = np.array(ship.pos)
		self.dt = dt
		self.mask = py.mask.from_surface(self.image)
		self.rot_center()
		self.name = name
		self.fuelmass = fuelinmiss
		self.prevunit = np.array([np.cos(np.deg2rad(ship.angle))+90,np.sin(np.deg2rad(ship.angle))+90])
		self.time = time.time()
		self.killme = False

	def rot_center(self,x=None):
		angle = x
		if x == None:
			angle = self.angle

		orig_rect = self.permimage.get_rect()
		rot_image = py.transform.rotate(self.permimage, angle - 90)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		self.image = rot_image
		if self.zoom != self.old_zoom:
			self.image = py.transform.scale(rot_image,
											(int(self.rectwidth * self.zoom), int(self.rectheight * self.zoom)))
			self.rect = self.image.get_rect()
			self.old_zoom = self.zoom
			print("Palyer zoom", self.zoom)
		else:
			self.image = rot_image
			self.rect = self.image.get_rect()

		self.rect = self.image.get_rect()
		self.rect.x = 520
		self.rect.y = 520

		self.mask = py.mask.from_surface(self.image)

	def update(self,planets):
		self.rot_center()

		force = rocketexhaustmass*rocketexhaustvelocity*dt
		self.fuelmass -= rocketexhaustmass*dt
		if(self.fuelmass>0):
			self.accel = force/(1+self.fuelmass)*np.array([np.cos(np.deg2rad(self.angle+90)),-np.sin(np.deg2rad(self.angle+90))])
		else:
			self.accel = np.linalg.norm([0.0,0.0])

		for i in planets:
			if py.sprite.collide_mask(self,i):
				self.move = False
			mpos = np.array([self.rect.x,self.rect.y])
			ppos = np.array([i.rect.x + 1000,i.rect.y+1000])
			r = ppos - mpos
			d = np.linalg.norm(r)
			if d < 2600:
				#print("Affected")
				G = (i.mass/(d**2))*r/d
				#print(G,self.vel)
				self.vel += np.array(G*dt,dtype =float)

		if(self.move==False):
			#self.vel = np.array([0,0])
			self.killme = True
		#	print("Missile",self.name," destroyed")


		unit = self.prevunit
		v = self.vel / np.linalg.norm(self.vel)
		if np.linalg.norm(self.vel)>0:
			unit = self.vel

		ca = np.rad2deg(np.arccos(v[0]))
		sa = np.rad2deg(np.arcsin(v[1]))


		#######################################
		self.vel += np.array(self.accel*dt,dtype=int)
		self.pos += self.vel*dt

		self.rect.x = self.pos[0] -(self.ships.pos[0]) + 520
		self.rect.y = self.pos[1] - (self.ships.pos[1]) + 520

		for i in planets:
			if py.sprite.collide_mask(self, i):
				#print(self.rect.x,self.rect.y,i.rect.x,i.rect.y)
				self.move = False
		#print(time.time()-self.time)
		if (time.time() - self.time) >missiledisappeartime:
			#print("TImedout ",self.name)
			self.killme = True