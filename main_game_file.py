# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from player import *
from cars import *
from music import *
from util_params import *
from background import *
from scoring_system import *

# pygame setup
pygame.init()

# Make screen properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background = place_background()

#Initialize all characters on screen and music
player = Player()
cars = Cars()
car_group = pygame.sprite.Group()
for i in range(10):
    car_group.add(Cars(randint(0,WIDTH), randint(0, 200)))
main_track()

game_state = True
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_state == True:
        player_movement = pygame.key.get_pressed()
        player.move(player_movement)

    ######RENDER YOUR GAME HERE#####
        screen.blit(background,(0,0))
        player.update()
        player.draw(screen)

        cars.update()
        cars.draw(screen)
        car_group.update()
        car_group.draw(screen)

        score = scoring_init()
        screen.blit(score, (350,0))

        if pygame.sprite.spritecollide(player, car_group, False):
            end_score = final_score()
            screen.fill("Blue")
            screen.blit(end_score, (220,300))
            game_state = False
    #####

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()