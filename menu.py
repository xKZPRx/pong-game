import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Menu:
    def __init__(self):
        self.bg = pygame.image.load("assets/images/background.png").convert()
        self.bg = pygame.transform.smoothscale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.title_font = pygame.font.Font(None, 150)
        self.main_font = pygame.font.Font(None, 100)

        self.options = ["Play", "Options", "Exit"]
        self.rects = []


    def draw(self, screen):
        self.rects = []
        screen.blit(self.bg, (0, 0))

        menu_text = self.title_font.render("MAIN MENU", True, "#00ddff")
        screen.blit(menu_text, ((SCREEN_WIDTH // 2) - (menu_text.get_width() // 2), 50))

        current_y = 200
        for option in self.options:
            # Base rect (fixed position)
            option_rect = pygame.Rect((SCREEN_WIDTH // 2) - 200, current_y, 400, 100)

            # Hover check
            mouse_pos = pygame.mouse.get_pos()
            if option_rect.collidepoint(mouse_pos):
                rect_surface = pygame.Surface((420, 100), pygame.SRCALPHA)
                rect_surface.fill((255, 255, 255, 50))
                hover_rect = rect_surface.get_rect(center=option_rect.center)
                screen.blit(rect_surface, hover_rect.topleft)

            else:
                rect_surface = pygame.Surface((400, 100), pygame.SRCALPHA)
                rect_surface.fill((255, 255, 255, 25))
                screen.blit(rect_surface, option_rect.topleft)

            # Draw text centered
            option_text = self.main_font.render(option, True, "#ffffff")
            text_x = option_rect.centerx - (option_text.get_width() // 2)
            text_y = option_rect.centery - (option_text.get_height() // 2)
            screen.blit(option_text, (text_x, text_y))

            current_y += 120
            self.rects.append((option_rect, option))