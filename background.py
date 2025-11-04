import pygame
from util_params import *

def place_background():
    terrain = 'attributes/backgroundColorGrass.png'
    terrain_surface = pygame.image.load(terrain)
    terrain_width = terrain_surface.get_width()
    terrain_background = pygame.Surface((WIDTH, HEIGHT))

    for x in range (0, WIDTH, terrain_width):
        terrain_background.blit(terrain_surface, (x,0))
        
    return terrain_background
