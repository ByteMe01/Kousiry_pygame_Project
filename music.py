import pygame

#Init mixer and load selected music file
pygame.mixer.init()
pygame.mixer.music.load('attributes/music.mp3')

# Function to play loaded track when called
def main_track():
    pygame.mixer.music.play()