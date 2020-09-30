import pygame
from constants import *
game_font = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(game_font, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.update()

    pygame.display.set_caption("Melon smash")
    main_menu = pygame.image.load("jungle_bg_main.png")
    main_menu_rect = main_menu.get_rect()
    screen.blit(main_menu, main_menu_rect)
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

    draw_text(screen, "GET READY!", 40, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.update()

    pygame.display.set_caption("Melon Strike")
    background = pygame.image.load("jungle_bg_.png")
    background_rect = background.get_rect()
    screen.blit(background, background_rect)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If x at the top gets pressed, quit game
                running = False
            if event.type == pygame.KEYDOWN:  # If escape button gets pressed, quit game
                if event.key == pygame.K_ESCAPE:
                    running = False

    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
    main()
