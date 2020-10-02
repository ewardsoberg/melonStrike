from constants import *
import os
import random
game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "assets")
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Melon Strike")
pygame.display.update()


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_folder, "jungle_bg_.png")).convert()
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_folder, "watermelon_.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 38))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30)

    def move_left(self):
        self.rect.x = self.rect.x - 5
        if self.rect.x < 150:
            self.rect.x = 150

    def move_right(self):
        self.rect.x = self.rect.x + 5
        if self.rect.x > 570:
            self.rect.x = 570


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_folder, "spear_1.png")).convert()
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 570)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(2, 10)
        self.speed_x = random.randrange(-3, 3)

    def update(self):

        self.rect.y += self.speed_y
        self.rect.y += 3
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(100, 570)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 5)


def main_menu():
    global screen

    game_menu = pygame.image.load(os.path.join(image_folder, "jungle_bg_main.png")).convert()
    game_menu_rect = game_menu.get_rect()
    screen.blit(game_menu, game_menu_rect)
    pygame.display.update()
    running = True
    while running:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            draw_text(screen, "Press [ENTER] To Begin", 30, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            draw_text(screen, "or [Esc] To Quit", 30, int(SCREEN_WIDTH / 2), int((SCREEN_HEIGHT / 2) + 40))
            pygame.display.update()

    screen.fill(BLACK)
    draw_text(screen, "ARE YOU READY!", 40, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.update()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(GAME_FONT, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def main():

    running = True
    menu_display = True
    while running:
        if menu_display:
            main_menu()
            pygame.time.wait(3000)
            break

    sprites_list = pygame.sprite.Group()
    pygame.display.update()
    background = Background()
    sprites_list.add(background)
    player = Player()
    sprites_list.add(player)
    sprites_list.update()
    enemies_list = []
    for _ in range(10):
        enemies = Enemies()
        enemies_list.append(enemies)
    sprites_list.add(enemies_list)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()

        sprites_list.update()
        screen.fill(BLACK)
        sprites_list.draw(screen)


        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
