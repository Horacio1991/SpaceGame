import pygame
from settings import WIDTH, HEIGHT, FPS, BLACK
from player import Player
from meteor import Meteor


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Inicio el módulo de sonido

        # Creo la pantalla con las dimensiones definidas en settings.py
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("UAI SPACESHIP")  # Nombre de la ventana

        # Cargar musica de fondo y sonido de explosión
        self.background_music = "assets/musica.mp3"
        self.explosion_sound = pygame.mixer.Sound("assets/explosion.mp3")
        self.explosion_sound.set_volume(0.7)

        self.clock = pygame.time.Clock()  # reloj para controlar los FPS
        self.running = True  # variable para controlar el bucle principal

        # Inicializar jugador y meteoritos
        self.player = Player()  # Crear el jugador
        self.meteors = []  # Crear una lista vacía para los meteoritos

        # Puntuación y highscore
        self.score = 0
        self.highscore = self.load_highscore()

        # Iniciar música de fondo
        self.play_background_music()

        # Temporizador para controlar la generación de meteoritos
        self.meteor_timer = 0

    # metodo para Reproducir música de fondo
    def play_background_music(self):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Reproducir en bucle

    # metodo para detener la música de fondo
    def stop_background_music(self):
        """Detiene la música de fondo."""
        pygame.mixer.music.stop()

    # metodo para cargar el puntaje máximo desde el archivo txt
    def load_highscore(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except (FileNotFoundError, ValueError):
            return 0

    # metodo para guardar el puntaje máximo en el archivo txt
    def save_highscore(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.highscore))

    # metodo para ejecutar el juego
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)  # Obtiene los FPS definidos en settings.py

        pygame.quit()

    # metodo para manejar los eventos del juego
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Salir del bucle principal

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

        # Actualizar meteoritos y verificar colisiones
        for meteor in self.meteors:
            meteor.update()
            if meteor.off_screen():  # Verificar si el meteorito salió de la pantalla
                self.meteors.remove(meteor)
                self.score += 1  # Incrementar puntuación

            if self.player.rect.colliderect(meteor.rect):
                self.handle_collision()

        # Controlar la frecuencia de generación de meteoritos
        self.meteor_timer += 1
        if self.meteor_timer >= 20:  # Generar un meteorito cada 20 frames
            self.meteors.append(Meteor())
            self.meteor_timer = 0  # Reiniciar el temporizador

    def handle_collision(self):
        """Maneja la colisión entre la nave y un meteorito."""
        self.stop_background_music()  # Detener la música de fondo
        self.explosion_sound.play()  # Reproducir sonido de explosión
        self.show_game_over()

    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)

        # Dibujar meteoritos
        for meteor in self.meteors:
            meteor.draw(self.screen)

        # Mostrar puntuación actual y highscore
        self.draw_text(f"Score: {self.score}", 30,
                       (255, 255, 255), WIDTH // 2, 10)
        self.draw_text(f"Highscore: {self.highscore}",
                       30, (255, 255, 255), WIDTH // 2, 40)

        pygame.display.flip()  # Actualizar pantalla

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def show_game_over(self):
        """Pantalla de Game Over."""
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()

        # Mostrar pantalla de Game Over
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 64, (255, 0, 0), WIDTH // 2, HEIGHT // 3)
        self.draw_text(f"Score: {self.score}", 40,
                       (255, 255, 255), WIDTH // 2, HEIGHT // 2)
        self.draw_text(f"Highscore: {self.highscore}", 40,
                       (255, 255, 255), WIDTH // 2, HEIGHT // 2 + 50)
        self.draw_text("Press ENTER to Restart", 30,
                       (255, 255, 255), WIDTH // 2, HEIGHT // 2 + 100)

        pygame.display.flip()

        # Esperar a que el usuario presione ENTER para reiniciar
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.reset_game()
                    waiting = False

    def reset_game(self):
        """Reinicia el juego."""
        self.score = 0
        self.player = Player()
        self.meteors = []
        self.play_background_music()  # Reiniciar la música de fondo


if __name__ == "__main__":
    game = Game()
    game.run()
