from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(ASSETS_FOLDER, "watermelon_.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2)
        self.rect.y = (SCREEN_HEIGHT - 45)
        self.lives = 3

    def move_left(self):
        self.rect.x = self.rect.x - 5
        if self.rect.x < 150:
            self.rect.x = 150

    def move_right(self):
        self.rect.x = self.rect.x + 5
        if self.rect.x > 570:
            self.rect.x = 570

    def control_player(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()