from const import *
import random

class Config:
    def __init__(self):
        self.coord = []
        self.create_stars()
    def create_stars(self):
        for x in range(int(WIDTH/15)):
            for y in range(int(HEIGHT/15)):
                self.coord.append((x*15 + random.randint(-8,8), y*15 + random.randint(-8,8), random.randint(0,255))) #coord: [x,y,color]
        return self.coord