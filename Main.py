import sys, pygame
from Mandelbrot import Mandelbrot
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(Mandelbrot.Mandelbrot(size, 50), screen.get_rect())
    pygame.display.flip()
