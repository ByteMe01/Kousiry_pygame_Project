# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

# Make screen properties
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


# You could use smaller images/props using the same process below
# Make Background
terrain = 'backgroundColorGrass.png'
terrain_surface = pygame.image.load(terrain)
terrain_width = terrain_surface.get_width()
terrain_height = terrain_surface.get_height()
terrain_background = pygame.Surface((WIDTH, HEIGHT))

# Loops over the background and places images on it
for x in range (0, WIDTH, terrain_width):
    terrain_background.blit(terrain_surface, (x,0))

# blit background to screen
screen.blit(terrain_background, (0,0))

#traffic_light = 'light.png'
#traffic_light_surface = pygame.image.load(traffic_light)
#traffic_light_width = traffic_light_surface.get_width()
#traffic_light_height = traffic_light_surface.get_height()
#traffic_light_image = pygame.Surface((WIDTH,HEIGHT))

#screen.blit(traffic_light_image, (100,100))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()