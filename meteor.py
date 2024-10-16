import pygame
import random
from settings import WIDTH, HEIGHT


class Meteor:
    def __init__(self):
        # Cargar y escalar la imagen del meteorito
        self.image = pygame.image.load("assets/Meteor.gif").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (50, 50))  # tamaño del meteorito en pixeles

        self.rect = self.image.get_rect()  # Area de colisión del meteorito
        # Posición inicial en x aleatoria
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = 0

        # Velocidad aleatoria para cada meteorito
        # Velocidades entre 3 y 8 píxeles por frame
        self.speed = random.randint(3, 8)

    # Actualizar la posición del meteorito
    def update(self):
        self.rect.y += self.speed  # Usar la velocidad aleatoria

    # Verificar si el meteorito salió de la pantalla
    def off_screen(self):
        return self.rect.top > HEIGHT

    # dibuja el meteorito en la pantalla
    def draw(self, screen):
        screen.blit(self.image, self.rect)
