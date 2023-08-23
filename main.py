# importing Pygame and random 
import pygame
import random

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

# bg image 
background = pygame.image.load("sprites\espacio.png")

# display screen 
screen = pygame.display.set_mode(size)

#player function
player_x = 370
player_y = 500
player_img = pygame.image.load("sprites/nave-1.png")
player_x_change = 0
player_y_change = 0
def player(x,y):
    screen.blit(player_img, (x,y))

#enemy function 
enemy_x = 360
enemy_y = 30
enemy_img = pygame.image.load("sprites/nave-2.png")
enemy_x_change = 0.4
enemy_y_change = 30
def enemy(x,y):
    screen.blit(enemy_img, (x,y))

# bala function
bala_img = pygame.image.load("./sprites/bala-laser.png")
bala_x = 370
bala_y = 500
bala_y_change = 10
bala_x_change = 0
bullet_state = True
def bala(x,y):
    screen.blit(bala_img, (x,y))

def fire(x,y):
    global bullet_state
    bullet_state = False
    screen.blit(bala_img, (x, y))

# game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard inputs
        if event.type == pygame. KEYDOWN :
            if event. key == pygame.K_LEFT :
                player_x_change = -0.5
            if event. key == pygame.K_RIGHT :
                player_x_change = 0.5
            if event.key  == pygame.K_SPACE:
                fire(bala_x, bala_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT :
                player_x_change = 0
            if event.key == pygame.K_RIGHT :
                player_x_change = 0

    # blit of the background 
    screen.blit(background, (0,0))

    # player movements
    player_x += player_x_change
    
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736 :
        player_x = 736
    #bala function
    
    bala(bala_x,bala_y)

    # blit of the player
    player(player_x,player_y) 

    # blit of the enemy
    enemy(enemy_x, enemy_y)

    # enemy movements
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.4
        enemy_y += enemy_y_change
    
    elif enemy_x >= 736 :
        enemy_x_change = -0.4
        enemy_y += enemy_y_change
    
    if bullet_state == False:
         fire(player_x, player_y)
         bala_y -= bala_y_change
    # update the window
    pygame.display.flip()
pygame.quit()

