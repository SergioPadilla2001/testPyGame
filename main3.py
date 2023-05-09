import pygame
import os

pygame.init()
GRIS_CLARO = (200, 200, 200)
# Crear la pantalla del juego.
pantalla = pygame.display.set_mode((800, 600))

# Nombre de la pantalla del juego.
pygame.display.set_caption("TEST")

iconos = pygame.image.load(os.path.join('imagenes', 'hero.png'))
pygame.display.set_icon(iconos)

# Define el tamaño de la pantalla
size = (700, 500)
# Crea la pantalla
screen = pygame.display.set_mode(size)
# Limpia la pantalla
screen.fill(GRIS_CLARO)


# Mantener la pantalla hasta que se le diga al programa que se cierre.
juego = True
while juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego = False