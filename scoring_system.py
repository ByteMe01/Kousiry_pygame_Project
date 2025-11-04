import pygame
pygame.init()

game_state = True
start_time = pygame.time.get_ticks()
score_font = pygame.font.Font("attributes/ComicStrip-KG3p.ttf", 100)

def scoring_init():
    if game_state == True:
        active_age = (pygame.time.get_ticks() - start_time)/1000
        score_system = f"Score: {int(active_age)}"
        score_surface = score_font.render(score_system, False, (0,0,0))
        return score_surface