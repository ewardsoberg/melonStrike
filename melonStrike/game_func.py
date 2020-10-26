from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Melon Strike")
pygame.display.update()


background = pygame.image.load(os.path.join(ASSETS_FOLDER, "jungle_bg_.png")).convert()
background_rect = background.get_rect()
lives_image = pygame.image.load(os.path.join(ASSETS_FOLDER, "watermelon_.png")).convert()
lives_image = pygame.transform.scale(lives_image, (50, 40))
lives_image.set_colorkey(WHITE)


def main_menu():
    global screen

    game_menu = pygame.image.load(os.path.join(ASSETS_FOLDER, "jungle_bg_main.png")).convert()
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
            draw_text(screen, "[<-] Use the arrows to move [->]", 30, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100)
            draw_text(screen, "Avoid the spears", 30, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 70)
            draw_text(screen, "Press [ENTER] To Begin", 30, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100)
            draw_text(screen, "or [Esc] To Quit", 30, int(SCREEN_WIDTH / 2), int((SCREEN_HEIGHT / 2) + 150))
            pygame.display.update()

    screen.fill(BLACK)
    draw_text(screen, "ARE YOU READY!?", 40, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.update()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(GAME_FONT, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (int(x), int(y))
    surf.blit(text_surface, text_rect)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 55 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def read_high_score():
    scores = open("assets/high_score.txt", "r").readlines()
    return [int(score.strip()) for score in scores if score.strip()]


def write_high_score(new_score, scores):
    scores.append(new_score)
    scores.sort(reverse=True)
    with open("assets/high_score.txt", "w") as file:
        for value in scores[:5]:
            file.write(str(value) + '\n')
