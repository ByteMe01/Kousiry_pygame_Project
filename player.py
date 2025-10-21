from util_params import PLAYER_HEIGHT, PLAYER_WIDTH
import pygame

class Player():
    def __init__(self, x = PLAYER_WIDTH, y = PLAYER_HEIGHT):
        self.fp = 'attributes/player_walk.png'
        self.player = pygame.image.load(self.fp)
        scale_size = (100,100)
        self.image = pygame.transform.scale(self.player, scale_size)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # center rect
        self.rect.center = (x,y)
        self.vx = 3 # x velocity

    def update(self):
        #move character
        #update character rect position
        self.rect.center = (self.x, self.y)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.vx
        if keys[pygame.K_RIGHT]:
            self.x += self.vx

    def draw(self, screen):
        # blit character to screen
        screen.blit(self.image, self.rect)