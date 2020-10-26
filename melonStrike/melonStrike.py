from game_func import *
from melon import Player
from spear import Enemies


def main():
    current_score = 0
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
        while True:
            no_collide = True
            enemy = Enemies()
            for e in enemies_list:
                if enemy.rect.colliderect(e):
                    no_collide = False
                    break
            if no_collide:
                enemies_list.append(enemy)
                break

    sprites_list.add(enemies_list)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.control_player()

        for e in enemies_list:
            if e.is_outside():
                current_score += 1
                if current_score > 50:
                    enemy.level_up(4, 8)
                if current_score > 100:
                    enemy.level_up(8, 12)
                if current_score > 200:
                    enemy.level_up(12, 16)
            if e.rect.colliderect(player.rect):
                e.rect.bottom = 0
                player.lives -= 1
        if player.lives == 0 and pygame.time.wait(1000):
            high_score = read_high_score()
            write_high_score(current_score, high_score)
            screen.fill(BLACK)
            draw_text(screen, "GAME OVER!", 40, SCREEN_WIDTH / 2, 100)
            draw_text(screen, "YOUR HIGH SCORES: ", 40, SCREEN_WIDTH / 2, 150)
            for i, score in enumerate(high_score[:5]):
                user = i + 1
                hs = score
                draw_text(screen, f"{user}: {hs}", 40, SCREEN_WIDTH / 2, 200 + (i * 40))
            pygame.display.update()
            pygame.time.wait(3000)
            main()

        sprites_list.update()
        screen.blit(background, background_rect)
        sprites_list.draw(screen)
        draw_text(screen, f"SCORE: {str(current_score)}", 25, SCREEN_WIDTH - SCREEN_WIDTH + 80,
                  SCREEN_HEIGHT - SCREEN_HEIGHT + 10)
        draw_lives(screen, 630, 5, player.lives, lives_image)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
