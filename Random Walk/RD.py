import pygame,sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
font=pygame.font.SysFont("arial",16)
font_height=font.get_linesize()
event_text= []

while True:
    event=pygame.event.wait()
    event_text.append(str(event))
    event_text=event_text[-480//font_height:]

    if event.type == QUIT:
        sys.exit()
    
    screen.fill((255,255,255))
    y=480-font_height
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,0,0)),(0,y))
        y-=font_height
    pygame.display.update()

