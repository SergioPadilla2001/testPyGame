import pygame
import random

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mi Juego")

done = False

clock = pygame.time.Clock()

x = 50
y = 50

speed_x = 5
speed_y = 5

rect_size = 50

color = (255, 0, 0)  # Color inicial: rojo

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica si se hizo clic en el cuadrado
            mouse_pos = pygame.mouse.get_pos()
            if x <= mouse_pos[0] <= x + rect_size and y <= mouse_pos[1] <= y + rect_size:
                # Cambia el color a uno aleatorio
                color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    x += speed_x
    y += speed_y

    if x + rect_size > size[0] or x < 0:
        speed_x *= -1
    if y + rect_size > size[1] or y < 0:
        speed_y *= -1

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color, [x, y, rect_size, rect_size])  # Dibuja el cuadrado con el color actual

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
