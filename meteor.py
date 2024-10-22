import pygame
import random
from settings import WIDTH, HEIGHT


class Meteor:
    def __init__(self):
        # Cargar y ajustar tamaño a la imagen del meteorito
        self.image = pygame.image.load("sprites/Meteor.gif").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (50, 50))  # tamaño del meteorito en pixeles

        self.rect = self.image.get_rect()  # area de colisión del meteorito
        # Posición aleatoria en la parte superior de la pantalla para cada meteorito
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = 0

        # Velocidad aleatoria para cada meteorito
        # Velocidades entre 3 y 10 píxeles por frame
        self.speed = random.randint(3, 10)

    # Mover el meteorito hacia abajo
    def update(self):
        self.rect.y += self.speed

    # Verificar si el meteorito salió de la pantalla
    def off_screen(self):
        return self.rect.top > HEIGHT

    # dibuja el meteorito en la pantalla
    def draw(self, screen):
        screen.blit(self.image, self.rect)
