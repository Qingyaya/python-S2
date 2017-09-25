# -*- coding: utf-8 -*-
import pygame

def main():
    pygame.init()
    screen=pygame.display.set_mode([480,480])
    running=True
    while running:
        screen.fill([0,0,0])
        pygame.draw.circle(screen,[255,0,0],[100,100],10,0)
        pygame.draw.arc(screen,[0,255,255],[200,100,100,20],20,100,10)
        pygame.draw.rect(screen,[0,255,255],[280,300,80,5],0) #最后一个参数是默认参数 默认参数为0
        pygame.draw.polygon(screen,[200,125,125],((100,30),(100,50),(120,30),(150,80),(100,30)),0)
        pygame.draw.aaline(screen,[0,255,0],[0, 0],[480, 480],True)
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()