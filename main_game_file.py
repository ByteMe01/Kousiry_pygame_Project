#Import required libraries
import pygame
from random import randint
from player import *
from cars import *
from music import *
from util_params import *
from background import *
from scoring_system import *
from title_screen import *

# pygame setup
pygame.init()

# Make screen properties66
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background = place_background() 

#Initialize all characters on screen and music
player = Player()
cars = Cars()
car_group = pygame.sprite.Group()
for i in range(11):
    car_group.add(Cars(randint(0,WIDTH), randint(0, 200)))
main_track()
pregame_audio()


#Set conditional flags for game operation
game_state = False
running = True
space_pressed = False

#display title screen + instructions
title_background = place_title_background()
screen.blit(title_background, (0,0))
title = menu()
user_instruction_1 = instruction_1()
user_instruction_2 = instruction_2()
screen.blit(title, (220,0))
screen.blit(user_instruction_1, (295,400))
screen.blit(user_instruction_2, (260,600))

#Start game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if player presses spacebar, game starts and space no longer functional
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not space_pressed:
                t0 = pygame.time.get_ticks()
                game_state = True
                space_pressed = True
                game_start()

    # Once spaced is pressed, the actual game can run
    if game_state:            
        player_movement = pygame.key.get_pressed()
        player.move(player_movement)

        #Set Screen
        screen.blit(background,(0,0))

        #Set Player and Player Movement
        player.update()
        player.draw(screen)

        #Set Cars and Car Generation
        cars.update()
        cars.draw(screen)
        car_group.update()
        car_group.draw(screen)

        # Set scoring system by assigning same number value to two variables for active score and final score
        score, last_score = scoring_init(t0)
        screen.blit(score, (350,0))

        #Set condition that ends game and displays final score
        if pygame.sprite.spritecollide(player, car_group, False):
            end_score = final_score(last_score)
            player_choice = player_input()
            screen.blit(title_background, (0,0))
            screen.blit(end_score, (220,150))
            game_state = False
            game_over()
            end_main_track()

    # flip() the display to put your work on screen
    pygame.display.flip()

    #FPS Limit to 60 FPS
    clock.tick(60)

pygame.quit()