import pygame
from util_params import CAR_HEIGHT, CAR_WIDTH
from random import randint

class Cars:
    def __init__(self, x = CAR_WIDTH, y = CAR_HEIGHT):
        self.fp = 'attributes/hotdog.png'
        self.car = pygame.image.load(self.fp)
        car_scaling = (75, 75)
        self.image = pygame.transform.scale(self.car, car_scaling)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.vy = 3
        
    def update(self):
        self.y += self.vy
        if self.y > 750:
            self.y = 0
            self.x = randint(0, 1000)
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


