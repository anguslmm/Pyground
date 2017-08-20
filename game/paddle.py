import pygame
from pygame import draw, display

class Paddle:
    def __init__(self, up_key, down_key, x=10, speed=1, color=(255, 255, 255)):
        self.up_key = up_key
        self.down_key = down_key
        self.y = pygame.display.get_surface().get_height()//2 - 25
        self.x = x
        self.speed = speed
        self.color = color
        self.y_speed = 0

    def draw(self):
        draw.rect(display.get_surface(), self.color, (self.x, self.y, 10, 50))

    def update(self):
        new_y = self.y + self.y_speed
        screen = display.get_surface()
        if new_y >= 0 and new_y <= screen.get_height() - 50:
            self.y += self.y_speed

    def move_down(self):
        self.y_speed = self.speed

    def move_up(self):
        self.y_speed = -self.speed

    def stop(self):
        self.y_speed = 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 10, 50)

    def handle_event(self, event: pygame.event):
        if event.type == pygame.KEYUP:
            if event.key == self.up_key and self.y_speed < 0:
                self.stop()
            if event.key == self.down_key and self.y_speed > 0:
                self.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == self.up_key:
                self.move_up()
            if event.key == self.down_key:
                self.move_down()
