
from planet import *
from map import *
from ship import *
from missile import *
from save import *
from Bar import *


class Display:
	def __init__(self,dbcom=""):
		py.init()
		self.s = None
		if dbcom == "create":
			self.s = Saver("create")
		else:
			self.s = Saver()

		self.initdisplayvar()
		
		self.win = py.display.set_mode((self.winx,self.winy))
		self.init_event_variables()
		self.run()
		self.spacewalk=np.array([0,0])


	def initdisplayvar(self):
		self.winx = 900
		self.winy = 800
		self.stopgame = False

	def init_event_variables(self):
		self.planets = []
		self.hero = py.sprite.Group()
		self.map = py.sprite.Group( )
		self.missiles = py.sprite.Group()
		self.satellites = py.sprite.Group()
		self.player = None
		self.fuelbar = None
		self.wkup = False
		self.wkdo = False
		self.wklf = False
		self.wkrh = False
		self.m_W_player = False
		self.m_S_player = False
		self.r_L_player = False
		self.r_R_player = False
		self.setorbital = False
		self.launchmissile = False
		pass;

	def setplanets(self):
		#initates the game settings and the sprites positions
		PG = PlanetGenerator()
		for i in PG.planets:
			self.planets.append(i)
			#sat = i.get_satellite()
			#self.satellites.add(sat)

	def sethero(self):
		i=None
		for i in self.planets:
			break;
		self.player = Player((i.rect.x,i.rect.y-i.radius));
		if loadlatest == True and self.s.dataexist():
			t =self.s.loadrecent()
			self.player.pos = np.array([t[1],t[2]])
			self.player.vel = np.array([t[3],t[4]])
			self.player.angle = t[5]
			self.player.accel = np.array([t[6],t[7]])

		self.hero.add(self.player)
		self.fuelbar = Bar()

	def setmap(self):
		self.map.add(Map(self.planets))

	def sprites_handler(self):
		pass;


	def eventhandler(self):
		for event in py.event.get():
			if event.type == py.QUIT:
				self.stopgame = True
			if event.type == 2:
				if event.key == py.K_UP:
					self.wkup = True
				if event.key == py.K_DOWN:
					self.wkdo = True
				if event.key == py.K_LEFT:
					self.wklf = True
				if event.key == py.K_RIGHT:
					self.wkrh = True
				if event.key == py.K_r:
					self.player.invert()
				if event.key == py.K_a:
					self.r_L_player = True
				if event.key == py.K_d:
					self.r_R_player = True
				if event.key == py.K_w:
					self.m_W_player = True
					self.player.accelerating = True
				if event.key == py.K_s:
					self.m_S_player = True
				if event.key == py.K_o:
					self.setorbital = True
				if event.key == py.K_SPACE:
					self.launchmissile = True
					self.player.missilecount +=1
				if event.key == py.K_t:
					self.player.autorotate = not self.player.autorotate

			if event.type == 3:
				if event.key == py.K_UP:
					self.wkup = False
				if event.key == py.K_DOWN:
					self.wkdo = False
				if event.key == py.K_LEFT:
					self.wklf = False
				if event.key == py.K_RIGHT:
					self.wkrh = False
				if event.key == py.K_a:
					self.r_L_player = False
				if event.key == py.K_d:
					self.r_R_player = False
				if event.key == py.K_w:
					self.m_W_player = False
					self.player.accelerating = False
				if event.key == py.K_s:
					self.m_S_player = False
				if event.key == py.K_q:
					self.stopgame = True
				if event.key == py.K_o:
					self.setorbital = False


	def affectgravity(self):
		nonthingtrue = True
		for i in self.planets:
			r = i.pos - self.player.pos

			dis = np.linalg.norm(r)
			if((dis > 900 and dis < 2600) and (not self.player.stopgravity)):

				g = i.mass/(dis)**2
				g_vec = g*r/dis
				self.player.vel += g_vec*dt
				if self.setorbital:
					self.player.setvelocity(np.sqrt(i.mass/dis))
					self.setorbital = False

	def respondevents(self):
		mpt = [0,0]
		if self.wkup:
			mpt[1]=-10
		if self.wkdo:
			mpt[1]=10
		if self.wklf:
			mpt[0]=-10
		if self.wkrh:
			mpt[0]=10

		if self.m_W_player or self.m_S_player:
			if self.m_W_player:
				self.player.accelerating = True
				self.player.accelerate()

				#print("accelerate")

			if self.m_S_player:
				#print("decelerate")
				self.player.decelerate()
		else:
			self.player.accelerating = False
			self.player.stopaccelerate()
			#print("stopping")

		if self.r_L_player:
			self.player.rotate(False)
		elif self.r_R_player:
			self.player.rotate(True)
		
		if not(self.r_L_player or self.r_R_player):
			self.player.stoprotate()

		if self.launchmissile:
			#print("missile launched")
			self.launchmissile = False
			self.missiles.add(Missile(self.player,str(self.player.missilecount)))

		for i in self.planets:
			i.update(2,self.player.pos)
		self.hero.update(self.planets)
		self.map.update(self.player.pos)
		self.missiles.update(self.planets)
		self.satellites.update(self.player.pos)


	def draw(self):

		for i in self.planets:
			self.win.blit(i.image,(i.rect.x,i.rect.y))
		#self.planets.draw(self.win)
		self.hero.draw(self.win)
		self.map.draw(self.win)
		self.missiles.draw(self.win)
		self.fuelbar.draw(self.win,self.player.fuel,100)
		#self.satellites.draw(self.win)
		#for i in self.satellites:
		#	i.draw(self.win)



	def run(self):
		self.stopgame=False
		self.setplanets()
		self.sethero()
		self.setmap()

		#testing
		while(not self.stopgame):
			self.win.fill((0,30,40))
			self.eventhandler()
			self.respondevents()
			for i in self.planets:
				#print(np.array(self.player.pos),np.array([i.rect.x,i.rect.y]))
				break
			self.draw()
			self.affectgravity()
			py.display.update()
			if self.stopgame == True:
				self.s.save(self.player)
				self.s.commit()
			#print(np.abs(self.player.angle-90)%360)

if __name__ == '__main__':
	import os
	files = os.listdir()
	if "mydb" in files:
		game = Display()
		#print("already")
	else:
		#print("creating")
		game = Display("create")