import pygame
from pygame.locals import * 


pygame.init()

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
fps = 60 #frame per second e.g. in flip book one page is one frame

ground_scroll = 0 
scroll_speed = 4 

#how to get path of any image
bg = pygame.image.load("images/bg.png")
ground_img = pygame.image.load("images/ground.png")

is_running = True 

while is_running:
    clock.tick(fps)
    screen.blit(bg, (0,0))
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()

