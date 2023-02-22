import pygame
import os

pygame.init()
# Crear la pantalla del juego.
pantalla = pygame.display.set_mode((800, 600))

# Nombre de la pantalla del juego.
pygame.display.set_caption("TEST")

iconos =    pygame.image.load(os.path.join('C:/Users/STI1/Desktop', 'hero.png'))
pygame.display.set_icon(iconos)



# Mantener la pantalla hasta que se le diga al programa que se cierre.
juego = True
while juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego = False