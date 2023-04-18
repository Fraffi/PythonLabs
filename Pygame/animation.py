import pygame
import math
from random import randint

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My animation')
clock = pygame.time.Clock()

def moveNdraw(poly, n, speed):
    minim = poly[0][0]
    for i in range(n):
        if minim > poly[i][0]: minim = poly[i][0]
        poly[i][0] += speed
    if minim > 800:
        for i in range(n):
            poly[i][0] -= 950
    pygame.draw.polygon(win, (255, 255, 255), poly)
        

def run_animation():
    FPS = 60

    isJump = False
    jumpCount = 10

    poly1 = [[150, 10], [180, 50], [90, 90], [30, 30]]
    poly2 = [[230, 90], [290, 170], [350, 110], [300, 70], [260, 60]]
    poly3 = [[450, 20], [470, 80], [400, 110], [370, 30]]
    poly4 = [[620, 110], [700, 160], [750, 150], [700, 70], [660, 80]]
    poly5 = [[500, 60], [580, 50], [620, 90], [570, 90]]
    poly6 = [[-10, 50], [0, 100], [-70, 150], [-110, 100], [-95, 70]]
    polygons = [poly1, poly2, poly3, poly4, poly5, poly6]
    
    angle = 0
    surf_x = 30
    surf_y = 505
    smile_x = 25
    smile_y = 25
    circle1_x = 22
    circle1_y = 20
    circle2_x = 37
    circle2_y = 20
    mouth_x = 20
    mouth_y = 25

    anim = True

    smile = pygame.Surface((50, 50), pygame.SRCALPHA)
    smile.fill((34, 139, 34, 0))
    rotated_smile = smile
    rect = smile.get_rect(center = (surf_x, surf_y))

    pygame.draw.circle(smile, (255, 215, 0), (smile_x, smile_y), 25)
    pygame.draw.circle(smile, (0, 0, 0), (circle1_x, circle1_y), 7)
    pygame.draw.circle(smile, (0, 0, 0), (circle2_x, circle2_y), 7)
    pygame.draw.arc(smile, (0, 0, 0), (mouth_x, mouth_y, 20, 20), math.pi, 2 * math.pi, 1)

    smile.set_alpha(0)
    
    while anim:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and surf_x > 40:
            surf_x -= 4
            angle += 4
            #rotated_smile = pygame.transform.flip(smile, 1, 0)
            rotated_smile = pygame.transform.rotate(smile, angle)
            rect = rotated_smile.get_rect(center = (surf_x, surf_y))
        if keys[pygame.K_RIGHT] and surf_x < 745:
            surf_x += 4
            angle -= 4
            #rotated_smile = pygame.transform.flip(smile, 1, 0)
            rotated_smile = pygame.transform.rotate(smile, angle)
            rect = rotated_smile.get_rect(center = (surf_x, surf_y))
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    surf_y += (jumpCount ** 2) / 3
                else:
                    surf_y -= (jumpCount ** 2) / 3
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
            
            

        win.fill((30, 144, 255))
        
        pygame.draw.rect(win, (34, 139, 34), (0, 500, 800, 500))
        pygame.draw.rect(win, (139, 69, 19), (0, 550, 800, 550))
        moveNdraw(poly1, 4, 2)
        moveNdraw(poly2, 5, 3)
        moveNdraw(poly3, 4, 2)
        moveNdraw(poly4, 5, 3)
        moveNdraw(poly5, 4, 2)
        moveNdraw(poly6, 5, 3)

        win.blit(rotated_smile, (rect.x, rect.y))
        
        pygame.display.update()

run_animation()
