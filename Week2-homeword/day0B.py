#user/bin/python
# -*- coding:utf-8 -*-

import pygame

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE *SIZE

snake = [[4,3],[5,3],[6,3]]
apple = [3,1]

def screen_show(screen):
    screen.fill([255,255,255])
    pygame.draw.circle(screen,[255,0,0],[apple[0]*SIZE+SIZE/2,apple[1]*SIZE+SIZE/2],SIZE/2)
    for body in snake:
        if snake.index(body) == 0:
            pygame.draw.rect(screen, [150, 150, 100], [body[0] * SIZE, body[1] * SIZE, SIZE - 1, SIZE - 1])
        else:
            pygame.draw.rect(screen,[156,165,181],[body[0]*SIZE,body[1]*SIZE,SIZE-1,SIZE-1])
    pygame.display.flip()

def w_down_cb():
    headx=snake[0][0]
    heady=snake[0][1]
    if heady-1 <> snake[1][1]:
        if heady <>0:
            for i in xrange(0,len(snake)):
                if i<len(snake)-2:
                    snake[-1-i]=snake[-1-i-1]
                elif i<len(snake)-1:
                    snake[-1-i]=[headx,heady]
                elif i==len(snake)-1:
                    snake[0][1]=heady-1
        else:
            for i in xrange(0, len(snake)):
                if i < len(snake) - 2:
                    snake[-1 - i] = snake[-1 - i - 1]
                elif i < len(snake) - 1:
                    snake[-1 - i] = [headx, heady]
                elif i == len(snake) - 1:
                    snake[0][1] = SCALE - 1
    else:
        pass

def a_down_cb():
    headx=snake[0][0]
    heady=snake[0][1]
    if headx-1<>snake[1][0]:
        if headx <>0:
            for i in xrange(0,len(snake)):
                if i<len(snake)-2:
                    snake[-1-i]=snake[-1-i-1]
                elif i<len(snake)-1:
                    snake[-1-i]=[headx,heady]
                elif i==len(snake)-1:
                    snake[0][0]=headx-1
        else:
            for i in xrange(0, len(snake)):
                if i < len(snake) - 2:
                    snake[-1 - i] = snake[-1 - i - 1]
                elif i < len(snake) - 1:
                    snake[-1 - i] = [headx, heady]
                elif i == len(snake) - 1:
                    snake[0][0] = SCALE - 1
    else:
        pass

def s_down_cb():
    headx=snake[0][0]
    heady=snake[0][1]
    if heady+1 <>snake[1][1]:
        if heady <>SCALE:
            for i in xrange(0,len(snake)):
                if i<len(snake)-2:
                    snake[-1-i]=snake[-1-i-1]
                elif i<len(snake)-1:
                    snake[-1-i]=[headx,heady]
                elif i==len(snake)-1:
                    snake[0][1]=heady+1
        else:
            for i in xrange(0, len(snake)):
                if i < len(snake) - 2:
                    snake[-1 - i] = snake[-1 - i - 1]
                elif i < len(snake) - 1:
                    snake[-1 - i] = [headx, heady]
                elif i == len(snake) - 1:
                    snake[0][1] =  1
    else:
        pass

def d_down_cb():
    headx=snake[0][0]
    heady=snake[0][1]
    if headx+1 <> snake[1][0]:

        if headx <>SCALE:
            for i in xrange(0,len(snake)):
                if i<len(snake)-2:
                    snake[-1-i]=snake[-1-i-1]
                elif i<len(snake)-1:
                    snake[-1-i]=[headx,heady]
                elif i==len(snake)-1:
                    snake[0][0]=headx+1
        else:
            for i in xrange(0, len(snake)):
                if i < len(snake) - 2:
                    snake[-1 - i] = snake[-1 - i - 1]
                elif i < len(snake) - 1:
                    snake[-1 - i] = [headx, heady]
                elif i == len(snake) - 1:
                    snake[0][0] =  1
    else:
        pass

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running = True
    while running:
        screen_show(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down_cb()
                elif event.key == pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()
    pygame.quit()


if __name__ == '__main__':
    main()