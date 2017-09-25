#/user/bin/python
# -*- coding:utf-8 -*-

import pygame

MOU_CON = False
board =pygame.Rect(280,400,80,5)
cricle = [100,100]
rad = 10

def draw_surface(screen):
    screen.fill([255,255,255])
    pygame.draw.rect(screen,[0,255,0],board)
    pygame.draw.circle(screen,[0,0,255],cricle,rad)
    pygame.display.flip()

def update_board():
    if MOU_CON :
        (x,y)=pygame.mouse.get_pos()
        board.centerx = x
        board.centery = y

def w_down_cb():
    if not MOU_CON:
        board.centery -= 5

def a_down_cb():
    if not MOU_CON:
        board.x -= 5

def s_down_cb():
    if not MOU_CON:
        board.centery += 5

def d_down_cb():
    if not MOU_CON:
        board.x += 5

def main():
    pygame.init()
    screen=pygame.display.set_mode([480,480])
    running=True
    while running:
        update_board()
        draw_surface(screen)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_w:
                    w_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key ==pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()
    pygame.quit()

if __name__ == '__main__':
    main()