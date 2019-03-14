import pygame as py 
from planet import *
from map import *;
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
		self.winx = 800
		self.winy = 800
		self.stopgame = False

	def init_event_variables(self):
		self.planets = py.sprite.Group();
		self.hero = py.sprite.Group();
		self.map = py.sprite.Group();
		self.player = None
		self.wkup = False;
		self.wkdo = False;
		self.wklf = False;
		self.wkrh = False;
		self.m_W_player = False;
		self.m_S_player = False;
		self.r_L_player = False;
		self.r_R_player = False;
		self.setorbital = False
		pass;

	def setplanets(self):
		#initates the game settings and the sprites positions
		PG = PlanetGenerator()
		for i in PG.planets:
			self.planets.add(i)
			#print(i.pos)
		#self.testplanet = Planet((0,0))
		#self.testgroup = py.sprite.Group();
		#self.testgroup.add(self.testplanet)
	def sethero(self):
		i=None
		for i in self.planets:
			break;
		self.player = Player((i.rect.x,i.rect.y));
		self.hero.add(self.player)
	def setmap(self):
		self.map.add(Map(self.planets));

		

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
				if event.key == py.K_w:
					self.m_W_player = True;
				if event.key == py.K_s:
					self.m_S_player = True;
				if event.key == py.K_o:
					self.setorbital = True;

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
				if event.key == py.K_w:
					self.m_W_player = False;
				if event.key == py.K_s:
					self.m_S_player = False;
				if event.key == py.K_q:
					self.stopgame = True
				if event.key == py.K_o:
					self.setorbital = False;

	def affectgravity(self):
		nonthingtrue = True
		for i in self.planets:
			r = i.pos - self.player.pos
			dis = np.linalg.norm(r)

			#print(dis)
			if((dis > 1010 and dis < 1600) and (not self.player.stopgravity) ):
				#print(dis)
				g = i.mass/(dis)**2
				g_vec = g*r/dis;
				self.player.vel += g_vec*0.01
				#print(np.sqrt(i.mass/dis))
				if self.setorbital:
					#print(self.setorbital,"Worked")
					self.player.setvelocity(np.sqrt(i.mass/dis))
					self.setorbital = False;
			if dis <= 1010:
				self.player.landed = True
		
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

		if self.m_W_player or self.m_S_player:
			if self.m_W_player:
				self.player.accelerate()
				#print("accelerate")
		
			if self.m_S_player:
				#print("decelerate")
				self.player.decelerate()
		else:
			self.player.stopaccelerate()


		if self.r_L_player:
			self.player.rotate(False)
		elif self.r_R_player:
			self.player.rotate(True)
		
		if not(self.r_L_player or self.r_R_player):
			self.player.stoprotate();
		


		#print(mpt)
		self.planets.update(1,mpt)
		self.planets.update(2,self.player.pos)
		self.hero.update();
		self.map.update(self.player.pos);
		#self.testgroup.update(mpt)

	def draw(self):
		#py.draw.circle(self.win,(255,255,255),(int(self.winx/2),int(self.winy/2) ),30,30)
		self.planets.draw(self.win)
		self.hero.draw(self.win)
		self.map.draw(self.win)
		#self.testgroup.draw(self.win)
		pass;
	
	def run(self):
		self.stopgame=False;
		self.setplanets()
		self.sethero();
		self.setmap();
		#testing
		while(not self.stopgame):
			self.win.fill((0,0,0))
			self.eventhandler()
			self.respondevents()
			for i in self.planets:
				#print(np.array(self.player.pos),np.array([i.rect.x,i.rect.y]))
				break;

			self.draw();
			self.affectgravity()
			py.display.update();


if __name__ == '__main__':
	game = Display()
	