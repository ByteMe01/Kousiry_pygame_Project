# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from player import *
from cars import *
from text_surface import *

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
for i in range(8):
    car_group.add(Cars(randint(0,WIDTH), randint(0, 200)))


start_time = pygame.time.get_ticks()
score_font = pygame.font.Font("attributes/ComicStrip-KG3p.ttf", 100)
game_state = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_state == True:
        player_movement = pygame.key.get_pressed()
        player.move(player_movement)

        active_age = (pygame.time.get_ticks() - start_time)/1000
        score_system = f"Score: {int(active_age)}"

        score_surface = score_font.render(score_system, False, (0,0,0))


        
        

    ######RENDER YOUR GAME HERE#####
        screen.blit(terrain_background, (0,0))
        player.update()
        player.draw(screen)
        cars.update()
        cars.draw(screen)
        screen.blit(score_surface, (350,0))
        
        

        car_group.update()
        car_group.draw(screen)

        if pygame.sprite.spritecollide(player, car_group, False):
            screen.fill("Black")
            game_state = False
    #####

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()