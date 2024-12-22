import pygame

from config import Config
from const import *
from space import Space

class Game:
    def __init__(self):
        self.config = Config() #coordinates [x,y,color]

        self.space = Space()

    def show_bg(self, surface):
        rect = (0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(surface,'black',rect)

        #Draw the stars
        for star in self.config.coord:
            rect = (star[0],star[1],1,1)
            pygame.draw.rect(surface,(star[2],star[2],star[2]),rect)
        
    def show_player(self,surface):
        player = self.space.player
        surface.blit(player.rotatedSurf,player.rotatedRect)