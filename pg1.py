#try pygame
import pygame
import sys
from pygame.locals import *

pygame.init()

size = width,height =1200,800
speed = [-2,1]
bg = (255, 255, 255)
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Welcome to game")

xm = pygame.image.load("xm.jpg")
position = xm.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1,0]
            if event.key ==K_RIGHT:
                speed = [1,0]
            if event.key ==K_UP:
                speed = [0,-1]
            if event.key ==K_DOWN:
                speed = [0,1]

    position = position.move(speed)

    if position.left < 0 or position.right > width:
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(xm,position)
    pygame.display.flip()

    
