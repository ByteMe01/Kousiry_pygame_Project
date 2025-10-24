# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from player import *
from cars import *

# pygame setup
pygame.init()

# Make screen properties
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


# Make Background
terrain = 'attributes/backgroundColorGrass.png'
terrain_surface = pygame.image.load(terrain)
terrain_width = terrain_surface.get_width()
terrain_height = terrain_surface.get_height()
terrain_background = pygame.Surface((WIDTH, HEIGHT))

# Loops over the background and places images on it
for x in range (0, WIDTH, terrain_width):
    terrain_background.blit(terrain_surface, (x,0))

player = Player()
cars = Cars()

car_group = pygame.sprite.Group()
for i in range(10):
    car_group.add(Cars(randint(0,WIDTH), randint(0, 200)))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    player_movement = pygame.key.get_pressed()
    player.move(player_movement)

    ######RENDER YOUR GAME HERE#####
    screen.blit(terrain_background, (0,0))
    player.update()
    player.draw(screen)
    cars.update()
    cars.draw(screen)

    car_group.update()
    car_group.draw(screen)

    #####

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()