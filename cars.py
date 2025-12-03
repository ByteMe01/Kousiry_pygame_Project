import pygame
from util_params import *
from random import randint, choice

#Cars Class as a Sprite
class Cars(pygame.sprite.Sprite):
    # Load car spawn location and list of car images to choice() from
    def __init__(self, x = CAR_WIDTH, y = CAR_HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.vehicles = [
            'attributes/hotdog.png',
            'attributes/bus.png',
            'attributes/scooter.png',
            'attributes/tractor.png',
            'attributes/vintage.png',
            'attributes/sports_yellow.png',
            'attributes/kart.png'
        ]
        #Randomly select an image from the list to load
        self.fp = choice(self.vehicles)
        self.car = pygame.image.load(self.fp)

        # Set car size, location, and velocity
        car_scaling = (75, 75)
        self.image = pygame.transform.scale(self.car, car_scaling)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.vy = 3 
        
        # Car movement
    def update(self):
        self.y += self.vy
        #Once car center y value is lower than the screen,
        #reset y value to top but put new x value in a random location
        if self.y > HEIGHT:
            self.y = 0
            self.x = randint(0, WIDTH)
        self.rect.center = (self.x, self.y)

    #Draw randomly selected car onto screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)


