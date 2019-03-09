import pygame as py 
from planet import *
from ship import *;
class Display:
	def __init__(self):
		py.init();
		self.initdisplayvar()
		
		self.win = py.display.set_mode((self.winx,self.winy))
		self.init_event_variables()
		self.run();
		self.spacewalk=np.array([0,0])

	def initdisplayvar(self):
		self.winx = 1000
		self.winy = 800 
		self.stopgame = False

	def init_event_variables(self):
		self.planets = py.sprite.Group();
		self.hero = py.sprite.Group();
		self.player = None
		self.wkup = False;
		self.wkdo = False;
		self.wklf = False;
		self.wkrh = False;
		self.r_L_player = False;
		self.r_R_player = False;
		pass;

	def setplanets(self):
		#initates the game settings and the sprites positions
		PG = PlanetGenerator()
		for i in PG.planets:
			self.planets.add(i)

		#self.testplanet = Planet((0,0))
		#self.testgroup = py.sprite.Group();
		#self.testgroup.add(self.testplanet)
	def sethero(self):
		self.player = Player();
		self.hero.add(self.player)

	def sprites_handler(self):
		pass;


	def eventhandler(self):
		for event in py.event.get():
			if event.type == py.QUIT:
				self.stopgame = True;
			if event.type == 2:
				if event.key == py.K_UP:
					self.wkup = True;
				if event.key == py.K_DOWN:
					self.wkdo = True;
				if event.key == py.K_LEFT:
					self.wklf = True;
				if event.key == py.K_RIGHT:
					self.wkrh = True;
				if event.key == py.K_r:
					self.player.invert();
				if event.key == py.K_a:
					self.r_L_player = True;
				if event.key == py.K_d:
					self.r_R_player = True;
					
			if event.type == 3:
				if event.key == py.K_UP:
					self.wkup = False;
				if event.key == py.K_DOWN:
					self.wkdo = False;
				if event.key == py.K_LEFT:
					self.wklf = False;
				if event.key == py.K_RIGHT:
					self.wkrh = False;
				if event.key == py.K_a:
					self.r_L_player = False;
				if event.key == py.K_d:
					self.r_R_player = False;
				
	def respondevents(self):
		mpt = [0,0]
		if self.wkup:
			mpt[1]=-100
		if self.wkdo:
			mpt[1]=100
		if self.wklf:
			mpt[0]=-100
		if self.wkrh:
			mpt[0]=100
		if self.r_L_player:
			self.player.rotate(True)
		elif self.r_R_player:
			self.player.rotate(False)
		
		if not(self.r_L_player or self.r_R_player):
			self.player.stoprotate();

		#print(mpt)
		self.planets.update(mpt)
		self.hero.update();
		#self.testgroup.update(mpt)
	def draw(self):
		#py.draw.circle(self.win,(255,255,255),(int(self.winx/2),int(self.winy/2) ),30,30)
		self.planets.draw(self.win)
		self.hero.draw(self.win)
		#self.testgroup.draw(self.win)
		pass;

	def run(self):
		self.stopgame=False;
		self.setplanets()
		self.sethero();
		#testing
		while(not self.stopgame):
			self.win.fill((0,0,0))
			self.eventhandler()
			self.respondevents()
			for i in self.planets:
				print(i.rect.x,i.rect.y)
				break;
			self.draw();
			
			py.display.update();


if __name__ == '__main__':
	game = Display()
	