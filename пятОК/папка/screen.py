import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.infoObject = pygame.display.Info()
        self.WIDTH, self.HEIGHT = self.infoObject.current_w, self.infoObject.current_h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Цветовой экран")
        self.font = pygame.font.Font(None, 74)

    def fill_color(self, color):
        self.screen.fill(color)

    def update(self):
        pygame.display.flip()

    def get_size(self):
        return self.WIDTH, self.HEIGHT

    def draw_text(self, text, position, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)

    def draw_square(self, position, size, color):
        pygame.draw.rect(self.screen, color, (position[0], position[1], size, size))
