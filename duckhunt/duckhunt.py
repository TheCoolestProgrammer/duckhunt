import pygame
import random
import sys
pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
x = screen_width // 2
y = screen_height // 2
len_circle = 40
speed = 40
ducks = []
duck_width = 180
duck_height = 100
duck_speed = 5
level =15
count = 0
need_to_new_level = 200
font = pygame.font.SysFont("comicsansms", 40)
circle = pygame.image.load("circle.png")
duck =pygame.image.load("duck.png")
duck2 = pygame.image.load("duck2.png")
duck3 =pygame.image.load("duck3.png")
duck4 = pygame.image.load("duck4.png")
bg = pygame.image.load("forest.png")
duck_death = pygame.image.load("duck_death.png")
dead_ducks = []
ammo = 3
# plane = pygame.image.load("plane.png")
# planes = 0
# planes2 = 0
# plane_x = 0
# plane_y = 0

while True:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == pygame.QUIT:
            pygame.quit()

    text = font.render(("count:" + str(count)+ " level:"+ str(level) + " need to new level:"+str(need_to_new_level) ), True, (0, 255, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and x-speed > 0:
        x -=speed
    if pressed[pygame.K_RIGHT] and x + speed+ len_circle < screen_width:
        x += speed
    if pressed[pygame.K_UP] and y-speed >60:
        y -= speed
    if pressed[pygame.K_DOWN] and y+speed+len_circle < screen_height:
        y += speed
    if len(ducks)//3 < level:
        for i in range(level - len(ducks) // 3):
            a = random.randint(0,1)
            b = random.randint(0+60, screen_height - duck_height-60)
            if a == 0:
                c = 0
            else:
                c = screen_width - duck_width
            if count >= need_to_new_level:
                ducks.append(a+2)
            else:
                ducks.append(a)
            ducks.append(b)
            ducks.append(c)

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 60))

    # if planes == 0 and planes2 == 0:
    #     a = random.randint(0,1)
    #     if a == 1:
    #         planes = 1
    #         planes2= 1
    # if planes == 1:
    #     if planes2 == 1:
    #         screen.blit(plane, (plane_x, plane_y))
    #         plane_x += 4
    #     else:
    #         b = random.randint(100, screen_height - duck_height - 60)
    #         plane_y = b
    #         # = random.randint(60,screen_height-60)
    #         planes2 = 1
    #     if plane_x > screen_width or plane_x < -duck_width:
    #         planes, planes2, plane_x,plane_y = 0,0,0,0

    i = 0
    while i < len(dead_ducks):

        if dead_ducks[i] > screen_height:
            for j in range(2):
                del (dead_ducks[i])
            continue
        screen.blit(duck_death, (dead_ducks[i + 1], dead_ducks[i]))
        dead_ducks[i] += duck_speed * 2
        i += 2

    #print(ducks)
    i = 0

    if count >= need_to_new_level:
        level += 1
        count = 0
        need_to_new_level *= 2


    while i < len(ducks):
        if ducks[i] == 0:
            ducks[i+2] += duck_speed
        elif ducks[i] == 1:
            ducks[i+2] -= duck_speed
        if ducks[i] == 2:
            ducks[i + 2] += duck_speed
        if ducks[i] == 3:
            ducks[i+2] -= duck_speed


        if pressed[pygame.K_e]:
            if ducks[i+2]+duck_width > x+(len_circle // 2) > ducks[i+2] and ducks[i+1]+duck_height > y+(len_circle // 2) > ducks[i+1]:
                if ducks[i] >1:
                    count += need_to_new_level // 4
                else:
                    count += 100
                dead_ducks.append(ducks[i+1])
                dead_ducks.append(ducks[i + 2])
                ammo += 2
                for j in range(3):
                    del(ducks[i])
                continue
            else:
                ammo -= 1
        if ducks[i + 2] > screen_width or ducks[i + 2] < -duck_width:
            for j in range(3):
                del(ducks[i])
            continue

        if ducks[i] == 0:
            screen.blit(duck, (ducks[i+2], ducks[i+1]))
        elif ducks[i] == 1:
            screen.blit(duck2, (ducks[i+2], ducks[i+1]))
        elif ducks[i] == 2:
            screen.blit(duck3, (ducks[i+2], ducks[i+1]))
        else :
            screen.blit(duck4, (ducks[i+2], ducks[i+1]))
        i += 3


    screen.blit(text, (0, 0))
    screen.blit(circle, (x,y))

    #pygame.draw.rect(screen, (255, 0, 0), (x, y, len_circle, len_circle))
    #print(ducks)
    #pygame.draw.rect(screen, (0, 255, 0), (ducks[0 + 2], ducks[0 + 1], duck_width, duck_height))
    pygame.display.update()