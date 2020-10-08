from constants import *
from spear import Enemies
from melon import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Melon Strike")
pygame.display.update()


background = pygame.image.load(os.path.join(image_folder, "jungle_bg_.png")).convert()
background_rect = background.get_rect()
lives_image = pygame.image.load(os.path.join(image_folder, "watermelon_.png")).convert()
lives_image = pygame.transform.scale(lives_image, (50, 40))
lives_image.set_colorkey(WHITE)


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


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 55 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def main():
    score = 0
    running = True
    menu_display = True
    while running:
        if menu_display:
            main_menu()
            pygame.time.wait(3000)
            break

    sprites_list = pygame.sprite.Group()
    pygame.display.update()
    player = Player()
    sprites_list.add(player)
    sprites_list.update()
    enemies_list = []
    for _ in range(10):
        enemies = Enemies()
        enemies_list.append(enemies)
    sprites_list.add(enemies_list)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.control_player()

        for enemies in enemies_list:
            if enemies.rect.top > SCREEN_HEIGHT:
                score += 1
            if enemies.rect.colliderect(player.rect):
                enemies.rect.bottom = 0
                player.lives -= 1
        """if player.lives == 0 and pygame.time.wait(1000):
            screen.fill(BLACK)
            draw_text(screen, "GAME OVER!", 40, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            pygame.display.update()
            pygame.time.wait(3000)
            running = False"""

        sprites_list.update()
        screen.blit(background, background_rect)
        sprites_list.draw(screen)
        draw_text(screen, f"SCORE: {str(score)}", 30, 60, 10)
        draw_lives(screen, 630, 5, player.lives, lives_image)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
