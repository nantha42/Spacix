import pygame as py
from pygame.locals import *

class Text:
    def __init__(self,surface):
        self.basicfont = py.font.SysFont(None,20)
        self.surface = surface
        pass

    def draw(self,position,text):
        text = self.basicfont.render(text, True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = position[0]
        textrect.centery = position[1]
        self.surface.blit(text,textrect)
