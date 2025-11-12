import pygame

#Init mixer and load selected music file
pygame.mixer.init()
pygame.mixer.music.load('attributes/music.mp3')
prep = pygame.mixer.Sound('attributes/prepare_yourself.ogg')
start = pygame.mixer.Sound('attributes/begin.ogg')
over = pygame.mixer.Sound('attributes/game_over.ogg')

# Function to play loaded track when called
def main_track():
    pygame.mixer.music.play()

# Function to fadeout music on game end
def end_main_track():
    pygame.mixer.music.fadeout(1000)

def pregame_audio():
    pygame.mixer.Sound.play(prep)

def game_start():
    pygame.mixer.Sound.play(start)

def game_over():
    pygame.mixer.Sound.play(over)

