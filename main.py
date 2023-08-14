# importing Pygame
import pygame

# initializate pygame
pygame.init()

# window size
screen_width = 800
screen_height = 600

# size variable

size = (screen_width, screen_height)

# Title
pygame.display.set_caption("Space Invaders  by Juan Andres")

# icon
icon = pygame.image.load("./sprites/nave-1.png")
pygame.display.set_icon(icon)

# display screen 
screen = pygame.display.set_mode(size)

# game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False