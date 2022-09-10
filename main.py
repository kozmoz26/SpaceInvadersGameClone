import random
# Add and initialize the pygame
import pygame

pygame.init()

# Add game window
screen = pygame.display.set_mode((800, 600))

# Background image
background = pygame.image.load("background.png")

# Game title and logo
pygame.display.set_caption("Space Invaders Clone")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(100, 700)
enemyY = random.randint(50, 150)
enemyX_change = 0.15
enemyY_change = 30


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game loop
running = True
while running:

    # Background Image
    screen.blit(background, (0, 0))

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.25
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.25
        if event.key == pygame.K_SPACE:
            fire_bullet(playerX, bulletY)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # Enemy movement
    if enemyX <= 0:
        enemyX_change = 0.15
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.15
        enemyY += enemyY_change

    playerX += playerX_change
    enemyX += enemyX_change

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Boundaries of the game
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
