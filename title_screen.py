import pygame
pygame.init()

title_font = pygame.font.Font("attributes/ComicStrip-KG3p.ttf", 100)
instruction_font = pygame.font.Font("attributes/ComicStrip-KG3p.ttf", 40)
instruction_font_2 = pygame.font.Font("attributes/ComicStrip-KG3p.ttf", 40)

def menu():
    title_surface = title_font.render("CRASH COURSE", True, (255,255,255))
    return title_surface

def instruction_1():
    instruction_1_surface = instruction_font.render("Press Spacebar to start!", True, (255,255,255))
    return instruction_1_surface

def instruction_2():
    instruction_surface_2 = instruction_font_2.render("Use arrow keys to move L & R", True, (255,255,255))
    return instruction_surface_2
    
