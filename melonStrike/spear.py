from constants import *
import random


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(ASSETS_FOLDER, "spear_1.png")).convert()
        self.image = pygame.transform.scale(self.image, (10, 100))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(150, 615)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(2, 4)

    def update(self):

        self.rect.y += self.speed_y
        self.rect.y += 3

    def is_outside(self):

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(150, 615)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(2, 4)
            return True
        return False

    def level_up(self, score):

        if score > 50:
            self.speed_y = random.randrange(4, 6)
        if score > 100:
            self.speed_y = random.randrange(6, 8)
        if score > 150:
            self.speed_y = random.randrange(8, 10)
        if score > 200:
            self.speed_y = random.randrange(10, 12)
        if score > 250:
            self.speed_y = random.randrange(12, 14)
        if score > 300:
            self.speed_y = random.randrange(14, 16)
        if score > 350:
            self.speed_y = random.randrange(16, 18)
        if score > 400:
            self.speed_y = random.randrange(18, 20)
