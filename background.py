import pygame
from util_params import *

#Function to load image file into pygame, match its dimensions to the screen
def place_background():
    terrain = 'attributes/backgroundColorGrass.png'
    terrain_surface = pygame.image.load(terrain)
    terrain_width = terrain_surface.get_width()
    terrain_background = pygame.Surface((WIDTH, HEIGHT))

    # Blit loaded image across the WIDTH of the screen
    # Can be used for adding other images randomly across screen using randint()
    for x in range (0, WIDTH, terrain_width):
        terrain_background.blit(terrain_surface, (x,0))
    return terrain_background

