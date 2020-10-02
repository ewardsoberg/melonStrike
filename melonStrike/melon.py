import pygame
from constants import *


class Melon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite().__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10


    def move_left(self, pixels):
        self.x_step -= pixels
        if self.x_step < 0:
            self.x_step = 0

    def move_right(self, pixels):
        self.x_step += pixels
        if self.x_step > 770:
            self.x_step = 770






