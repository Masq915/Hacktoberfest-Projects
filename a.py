import math
import random

import pygame
from pygame import mixer

pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon for the Game
pygame.display.set_caption("Space Invader: Spider-Man Edition")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Background Image
background = pygame.image.load('bg.png')

# Background Music
mixer.music.load("BgMusic.wav")
mixer.music.play(-1)

# Spidey
spideyImg = pygame.image.load('spidey.png')
spideyX = 370
spideyY = 480
spideyX_change = 0

# Our Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Web

# Ready - You can't see the web on the screen
# Fire - The web is currently moving

webImg = pygame.image.load('web.png')
webX = 0
webY = 480
webX_change = 0
webY_change = 2
web_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def spidey(x, y):
    screen.blit(spideyImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_web(x, y):
    global web_state
    web_state = "fire"
    screen.blit(webImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, webX, webY):
    distance = math.sqrt(math.pow(enemyX - webX, 2) + (math.pow(enemyY - webY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spideyX_change = -0.8
            if event.key == pygame.K_RIGHT:
                spideyX_change = 0.8
            if event.key == pygame.K_SPACE:
                if web_state is "ready":
                    webSound = mixer.Sound("WebSound.wav")
                    webSound.play()
                    # Get the current x cordinate of the spaceship
                    webX = spideyX
                    fire_web(webX, webY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spideyX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    spideyX += spideyX_change
    if spideyX <= 0:
        spideyX = 0
    elif spideyX >= 736:
        spideyX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.9
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.9
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], webX, webY)
        if collision:

            webY = 480
            web_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Web Movement
    if webY <= 0:
        webY = 480
        web_state = "ready"

    if web_state is "fire":
        fire_web(webX, webY)
        webY -= webY_change

    spidey(spideyX, spideyY)
    show_score(textX, testY)
    pygame.display.update()

