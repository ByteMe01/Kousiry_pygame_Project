import pygame

pygame.mixer.init()
pygame.mixer.music.load('attributes/music.mp3')

def main_track():
    pygame.mixer.music.play()