import pygame
import random

# Inicializa pygame
pygame.init()

# Define algunos colores
BLANCO = (255, 255, 255)
GRIS_CLARO = (200, 200, 200)
BLACK = (0, 0, 0)

# Definimos algunas constantes para el botón
WIDTH = 640
BUTTON_WIDTH = 190
BUTTON_HEIGHT = 50
BUTTON_COLOR = (255, 225, 155)
BUTTON_BORDER_COLOR = (0, 0, 0)
BUTTON_TEXT = 'Agregar cuadrado'

# Define el tamaño de la pantalla
size = (700, 500)

# Crea la pantalla
screen = pygame.display.set_mode(size)

# Define el título de la pantalla
pygame.display.set_caption("Mi Juego Pygame")

# Define la lista de cuadrados
square_list = []

# Define el tamaño del cuadrado
rect_size = 50

# Define la velocidad del movimiento del cuadrado
speed_x = 5
speed_y = 5

# Define el color del cuadrado
color = (255, 0, 0)

# Define el botón de agregar cuadrado
add_button_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - 10, 20, BUTTON_WIDTH, BUTTON_HEIGHT)

# Define la fuente del texto del botón de agregar cuadrado
add_button_font = pygame.font.SysFont('Arial', 20)

# Define la función para agregar un nuevo cuadrado en una posición aleatoria
def add_square():
    new_x = random.randint(0, size[0] - rect_size)
    new_y = random.randint(0, size[1] - rect_size)
    square_list.append((new_x, new_y, (255, 0, 0)))

# Define la función para obtener un color aleatorio
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Ciclo del juego
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Si el botón izquierdo del mouse está presionado
            if event.button == 1:
                # Verifica si se hizo clic en el botón de agregar cuadrado
                if add_button_rect.collidepoint(mouse_pos):
                    add_square()
                # Verifica si se hizo clic en un cuadrado
                for i, square in enumerate(square_list):
                    square_rect = pygame.Rect(square[0], square[1], rect_size, rect_size)
                    if square_rect.collidepoint(mouse_pos):
                        square_list[i] = (square[0], square[1], get_random_color())

    # Limpia la pantalla
    screen.fill(GRIS_CLARO)

    # Dibujamos el botón
    button_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - 10, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button_rect, 2)

    # Agregamos el texto al botón
    font = pygame.font.Font(None, 30)
    text_surface = font.render(BUTTON_TEXT, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # Actualiza la posición de los cuadrados
    for i, square in enumerate(square_list):
        x, y, color = square
        x += speed_x
        y += speed_y

        # Si el cuadrado llega al borde derecho o izquierdo de la pantalla
        if x + rect_size > size[0] or x < 0:
            speed_x = -speed_x

        # Si el cuadrado llega al borde inferior o superior de la pantalla
        if y + rect_size > size[1] or y < 0:
            speed_y = -speed_y

        # Actualiza la posición del cuadrado
        square_list[i] = (x, y, color)

        # Dibuja el cuadrado en la pantalla
        pygame.draw.rect(screen, color, [x, y, rect_size, rect_size])

    # Actualiza la pantalla
    pygame.display.flip()

    # Establece el número de fotogramas por segundo
    clock.tick(60)

# Cierra pygame
pygame.quit()
