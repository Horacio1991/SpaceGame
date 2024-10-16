import pygame
from settings import WIDTH, HEIGHT


class Player:
    def __init__(self):
        # Cargar y escalar la imagen del jugador
        self.image = pygame.image.load("assets/SpaceShip.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (50, 50))  # tamaño de la nave en pixeles

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2  # Posición inicial en el centro
        self.rect.bottom = HEIGHT - 10  # Posición inicial en la parte inferior

    # Método para mover la nave
    def handle_input(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Dibujar la nave en la pantalla
