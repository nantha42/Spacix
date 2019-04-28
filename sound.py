import pygame as py
import numpy as np
import time

class Sound:
    def __init__(self):
        self.songs = ["scores/New_age.ogg","scores/thrust1.ogg","scores/offthrust.ogg"]
        self.thrust = py.mixer.Sound(self.songs[1])
        self.offthrust = py.mixer.Sound(self.songs[2])
    def theme(self):
        music = py.mixer.Sound(self.songs[0])
        music.set_volume(0.1)
        music.play(-1)

    def thrusts(self):
        self.offthrust.stop()
        self.thrust.set_volume(0.3)
        self.thrust.play(-1)

    def stopthrusts(self):
        self.offthrust.set_volume(0.2)
        self.offthrust.play()
        self.thrust.stop()

