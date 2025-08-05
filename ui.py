import pygame

class Button:
    def __init__(self, text, rect, font, bg_color, text_color):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color


    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)