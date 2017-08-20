import pygame
import sys

from game.ball import Ball
from game.paddle import Paddle

pygame.init()

size = width, height = 640, 480
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = Ball()

paddle1 = Paddle(pygame.K_w, pygame.K_s)
paddle2 = Paddle(pygame.K_UP, pygame.K_DOWN, width - 20, 1)
actors = [paddle1, paddle2, ball]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for x in actors:
                x.handle_event(event)

    screen.fill(black)
    ball.check_collision(paddle2)
    ball.check_collision(paddle1)
    for x in actors:
        x.update()
        x.draw()
    pygame.display.flip()

