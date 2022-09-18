import pygame
from random import randint
import time

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('pyong')

running = True
screen.fill((0, 0, 0))

clock = pygame.time.Clock()

p1s = 0
p2s = 0
y1 = 300
y2 = 300
xb = 300
yb = 300
Vx = randint(1, 2)
Vy = randint(-2, 2)
font = pygame.font.Font('Minecraft-Bold.otf', 96)

while running:

    screen.fill((0, 100, 255))

    p1 = pygame.draw.rect(screen, (255, 255, 255), [100, y1, 25, 100])
    p2 = pygame.draw.rect(screen, (255, 255, 255), [500, y2, 25, 100])
    ball = pygame.draw.rect(screen, (255, 255, 255), [xb, yb, 25, 25])
    p1sc = font.render(str(p1s), True, (255, 255, 255))
    p2sc = font.render(str(p2s), True, (255, 255, 255))

    clock.tick(60)

    xb = xb + Vx
    yb = yb + Vy

    if(yb <= 0):
        Vy = -Vy
        yb = yb + Vy

    if(yb >= 575):
        Vy = -Vy
        yb = yb + Vy

    if(xb <= 0 or xb >= 600):
        if(xb <= 0):
            p2s = p2s + 1
        if(xb >= 550):
            p1s = p1s + 1
        time.sleep(0.2)
        xb = 300
        yb = 300
        Vx = randint(1, 2)
        Vy = randint(-2, 2)

    if(ball.colliderect(p1) or ball.colliderect(p2)):
        Vx = -Vx
        Vy = randint(-2,2)
        xb = xb + (Vx * 2)
        yb = yb + (Vy * 2)

    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                y2 -= 25
                if (y2 <= 0):
                    y2 = 0

            if event.key == pygame.K_DOWN:
                y2 += 25
                if (y2 >= 500):
                    y2 = 500

            if event.key == pygame.K_w:
                y1 -= 25
                if (y1 <= 0):
                    y1 = 0

            if event.key == pygame.K_s:
                y1 += 25
                if (y1 >= 500):
                    y1 = 500

    screen.blit(p1sc, (150, 10))
    screen.blit(p2sc, (414, 10))
    pygame.display.update()
    pygame.display.flip()