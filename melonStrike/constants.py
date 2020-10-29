import os
import pygame

GAME_FOLDER = os.path.dirname(__file__)
ASSETS_FOLDER = os.path.join(GAME_FOLDER, "assets")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POWER_UP_TIME = 5000
BAR_LENGTH = 100
BAR_HEIGHT = 10

GAME_FONT = pygame.font.match_font('arial')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
