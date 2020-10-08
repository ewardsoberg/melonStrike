from constants import *


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_folder, "spear_1.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(150, 620)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(2, 10)

    def update(self):

        self.rect.y += self.speed_y
        self.rect.y += 3
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(150, 620)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 5)
