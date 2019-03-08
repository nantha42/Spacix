import pygame as py 

class Display:
	def __init__(self):
		py.init();
		self.initdisplayvar()
		
		self.win = py.display.set_mode((self.winx,self.winy))
		self.init_event_variables()
		self.run();
	def initdisplayvar(self):
		self.winx = 600
		self.winy = 600 
		self.stopgame = False

	def init_event_variables(self):
		pass;
	
	def eventhandler(self):
		for event in py.event.get():
			if event.type == py.QUIT:
				self.stopgame = True;

	def draw(self):
		py.draw.circle(self.win,(255,255,255),(int(self.winx/2),int(self.winy/2) ),30,30)
		pass;

	def run(self):
		self.stopgame=False;
		while(not self.stopgame):
			self.eventhandler()
			self.draw();
			py.display.update();


if __name__ == '__main__':
	game = Display()
	game.run();