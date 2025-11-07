from util_params import PLAYER_HEIGHT, PLAYER_WIDTH
import pygame
from music import *

#Player Class
class Player(pygame.sprite.Sprite):
    #Set Player Spawn location
    def __init__(self, x = PLAYER_WIDTH, y = PLAYER_HEIGHT):
        #Load file into pygame
        self.fp = 'attributes/player_walk.png'
        self.player = pygame.image.load(self.fp)
        #Scale image and establish (x,y) position and velocity
        scale_size = (80,80)
        self.image = pygame.transform.scale(self.player, scale_size)
        self.walk_sound = pygame.mixer.Sound('attributes/footstep_grass_002.ogg')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.vx = 4

    #update character location on screen based on rect center values
    def update(self):
        self.rect.center = (self.x, self.y)
        
    # move() player using key input left and right to change velocity magnitude 
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.vx
            self.walk_sound.play()
        if keys[pygame.K_RIGHT]:
            self.x += self.vx
            self.walk_sound.play()
        # set left/right max boundaries that prevent player from leaving screen
        if self.x > 950:
            self.x = 950
        if self.x < 50:
            self.x = 50

    #blit character onto the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)