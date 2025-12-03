import pygame
pygame.init()

#Establish a starting time, init font 
score_font = pygame.font.Font("attributes/ComicStrip-KG3p.ttf", 100)
instruction_font = pygame.font.Font("attributes/ComicStrip-KG3p.ttf", 30)


# if game is running, score clock is running
# every second the player is alive, subtract that number with total time then render calculated value on screen
def scoring_init(start_time):
    active_age = (pygame.time.get_ticks() - start_time)/1000
    score_system = f"Score: {int(active_age)}"
    score_surface = score_font.render(score_system, False, (0,0,0))
    return score_surface, active_age

# This function took me a while to figure out
# Takes on the final value from scoring_init and displays that 
def final_score(final_score):
    final_score = f"Final Score: {int(final_score)}"
    final_score_surface = score_font.render(final_score, True, (0,0,0))
    return final_score_surface

def player_input():
    player_input = "Press space bar to play again or click x to quit"
    player_input_surface = instruction_font.render(player_input, False, (0,0,0))
    return player_input_surface