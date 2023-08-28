# importing Pygame and random and math
import pygame
import random
import math

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

# Score font 
score_font = pygame.font.Font("upheavtt.ttf", 32)

#variable score
score = 0

#position text in screen 
text_x = 10
text_y = 10 

# game over font 
go_x = 200
go_y = 250
 
#player function
player_x = 370
player_y = 500
player_img = pygame.image.load("sprites/nave-1.png")
player_x_change = 0
player_y_change = 0
def player(x,y):
    screen.blit(player_img, (x,y))

#enemy function 
enemy_x = []
enemy_y = []
enemy_img = []
enemy_x_change = []
enemy_y_change = []
number_enemies = 8

for item in range(number_enemies):
    enemy_img.append(pygame.image.load("nave-2.png"))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(50,150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)
def enemy(x,y, item):
    screen.blit(enemy_img[item], (x,y))

# bala function

bala_img = pygame.image.load("./sprites/bala-laser.png")
bala_x = 370
bala_y = 500
bala_y_change = 30
bala_x_change = 0
bullet_state = True
def bala(x,y):
    screen.blit(bala_img, (x,y))

def fire(x,y):
    global bullet_state
    bullet_state = False
    screen.blit(bala_img, (x, y))

#Collision
def is_collision (b_x, b_y, e_x, e_y):
    distance = math.sqrt((e_x - b_x)**2 + (e_y - b_y)**2)
    if distance < 27:
        return True
    else:
        return False

# Function of the text
def game_over(x,y) :
    go_text = score_font.render("GAME OVER",True,(55,0,0))
    screen.blit(go_text, (x,y))

def show_score(x,y) :
    go_text = score_font.render("SCORE: " + str(score),True,(255,255,255))
    screen.blit(go_text, (x,y))

# game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard inputs
        if event.type == pygame. KEYDOWN :
            if event. key == pygame.K_LEFT :
                player_x_change = -4
            if event. key == pygame.K_RIGHT :
                player_x_change = 4
            if event.key  == pygame.K_SPACE and bullet_state == True:
                bala_x = player_x
                fire(bala_x,bala_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT :
                player_x_change = 0
            if event.key == pygame.K_RIGHT:
                player_x_change = 0

    # blit of the background 
    screen.blit(background, (0,0))

    # player movements
    player_x += player_x_change
    
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736 :
        player_x = 736
    
    # blit of the player
    player(player_x,player_y) 

    for item in range(number_enemies ) :
    
        if enemy_y[item] > 440:
            for j in range (number_enemies) :
                enemy_y[j] = 2000
            
        collision = is_collision(bala_x, bala_y, enemy_x[item], enemy_y[item])
        if collision:
            bala_y = 500
            bullet_state = True
            enemy_x[item] = random.randint(0, 735)
            enemy_y[item] = random.randint(50, 150)
            score += 10 

        # blit of the enemy
        enemy(enemy_x[item], enemy_y[item], item)

        # enemy movements
        enemy_x[item] += enemy_x_change[item]
        if enemy_x[item] <= 0:
            enemy_x_change[item] = 3
            enemy_y[item] += enemy_y_change[item]
        
        elif enemy_x[item] >= 736 :
            enemy_x_change[item] = -3
            enemy_y[item] += enemy_y_change[item]
    
    if bullet_state == False:
         fire(bala_x, bala_y)
         bala_y -= bala_y_change
    
    if bala_y <= 0:
        bala_y = 500
        bullet_state = True
    
    # update the window
    show_score(text_x, text_y)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()

