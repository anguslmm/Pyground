import random

import pygame

from game.paddle import Paddle


class Ball:
    def __init__(self):
        self.speed = 3
        self.reset()


    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x)//10+5, int(self.y)//10+5), 5)

    def update(self):
        screen = pygame.display.get_surface()
        if self.x > screen.get_width()*10 or self.x < 0:
            self.reset()
        if self.y < 0 or self.y > screen.get_height()*10:
            self.y_speed = -self.y_speed

        self.y += self.y_speed
        self.x += self.x_speed

    def reset(self):
        screen = pygame.display.get_surface()
        pos_x = random.choice([-1, 1])
        pos_y = random.choice([-1, 1])
        self.x = screen.get_width()*10//2 - 5
        self.y = screen.get_height()*10//2 - 5
        angle = random.random()
        self.x_speed = angle * self.speed * pos_x
        self.y_speed = (1.0 - angle) * self.speed * pos_y

    def check_collision(self, paddle: Paddle):
        pad_rect = paddle.get_rect()
        this_rect = pygame.Rect(self.x//10, self.y//10, 10, 10)
        if this_rect.colliderect(pad_rect):
            self.x_speed = -self.x_speed

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.reset()