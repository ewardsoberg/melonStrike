import pygame
import os
import random

game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "assets")


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POWER_UP_TIME = 5000
BAR_LENGTH = 100
BAR_HEIGHT = 10

GAME_FONT = pygame.font.match_font('arial')

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
