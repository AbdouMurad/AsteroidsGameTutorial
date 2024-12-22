import math
import pygame

from const import *

class Player:
    def __init__(self, coord, direction = 0, velocity = [0,0]):
        self.coord = coord
        self.velocity = velocity
        self.direction = direction

        self.acceleration = 0
        self.force = 0
        self.mass = MASS
        self.health = HEALTH

        self.speed = math.sqrt(velocity[0]**2 + velocity[1]**2)

        self.img1 = pygame.image.load('assets/spaceship.png')
        self.img2 = pygame.image.load('assets/spaceship2.png')

        self.img = self.img1
        self.texture_rect = self.img.get_rect(center = self.coord)

        self.rotatedSurf = pygame.transform.rotate(self.img,self.direction)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = self.coord
    
    def apply_force(self,force,deltatime = 0):
        self.acceleration = force/self.mass

        self.velocity[0] += deltatime * self.acceleration * math.sin(self.direction*math.pi/180)
        self.velocity[1] += deltatime * self.acceleration * math.cos(self.direction*math.pi/180)

        displacementX = self.velocity[0]*deltatime
        displacementY = self.velocity[1] * deltatime

        self.coord[0] -= displacementX
        self.coord[1] -= displacementY

        self.speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

        self.rotatedSurf = pygame.transform.rotate(self.img, self.direction)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = self.coord
