import pygame
import sys
import time

from const import *
from game import Game
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Asteroids")
        self.game = Game()


    def mainloop(self):
        moveUp = False
        rotateLeft = False
        rotateRight = False


        prev_time = time.time()
        dt = 0

        game = self.game
        screen = self.screen 
        player = game.space.player
        while True:

            now = time.time()
            dt = now - prev_time
            prev_time = now

            game.show_bg(screen)
            game.show_player(screen)

            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.quit:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        moveUp = True
                    if event.key == pygame.K_a:
                        rotateLeft = True
                    elif event.key == pygame.K_d:
                        rotateRight = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        moveUp = False
                    if event.key == pygame.K_a:
                        rotateLeft = False
                    if event.key == pygame.K_d:
                        rotateRight = False


            if moveUp:
                player.apply_force(FORCE, deltatime = dt)

            if rotateLeft:
                player.direction += ROTATE_SPEED * dt
            if rotateRight: 
                player.direction -= ROTATE_SPEED*dt

main = Main()
main.mainloop()