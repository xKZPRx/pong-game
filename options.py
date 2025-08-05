import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from ui import Button


class Options:
    def __init__(self):
        self.bg = pygame.image.load("assets/images/background.png").convert()
        self.bg = pygame.transform.smoothscale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.title_font = pygame.font.Font(None, 100)
        self.subtitle_font = pygame.font.Font(None, 75)
        self.main_font = pygame.font.Font(None, 50)

        self.modes = ["vsPlayer", "vsBot"]
        self.mode_index = 1

        self.difficulties = ["Easy", "Medium", "Hard", "Extreme"]
        self.colors = ["#1eb700", "#f08c00", "#c10000", "#9800c6"]
        self.hover_colors = ["#168600", "#ad6500", "#8a0000", "#670087"]
        self.difficulty_index = 1

        self.rects = []


    def draw(self, screen):
        self.rects = []

        # Background
        screen.blit(self.bg, (0, 0))

        # Title
        options_text = self.title_font.render("OPTIONS", True, "#00ddff")
        screen.blit(options_text, ((SCREEN_WIDTH // 2) - (options_text.get_width() // 2), 50))

        # Mode
        mode_text = self.subtitle_font.render("Mode", True, "#ffffff")
        screen.blit(mode_text, ((SCREEN_WIDTH // 2) - (mode_text.get_width() // 2), 150))
        
        gap = 20
        button_width = 200
        total_width = button_width * 2 + gap
        start_x = (SCREEN_WIDTH // 2) - (total_width // 2)

        for i, mode in enumerate(self.modes):
            x = start_x + i * (button_width + gap)
            button_rect = pygame.Rect(x, 220, button_width, 50)

            # Hover check
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                button = Button(mode, button_rect, self.main_font, "#00a9c3", "#ffffff")

            else:
                button = Button(mode, button_rect, self.main_font, "#00ddff", "#ffffff")

            if i == self.mode_index:
                border_rect = button_rect.inflate(6, 6)
                pygame.draw.rect(screen, "#ffffff", border_rect, 1)
                
            button.draw(screen)
            self.rects.append((button_rect, mode))

        # Difficulty
        difficulty_text = self.subtitle_font.render("Difficulty", True, "#ffffff")
        screen.blit(difficulty_text, ((SCREEN_WIDTH // 2) - (difficulty_text.get_width() // 2), 320))

        gap = 10
        button_width = 150
        total_width = button_width * 4 + gap * 3
        start_x = (SCREEN_WIDTH // 2) - (total_width // 2)

        for i, (difficulty, color) in enumerate(zip(self.difficulties, self.colors)):
            x = start_x + i * (button_width + gap)
            button_rect = pygame.Rect(x, 390, button_width, 50)

            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                hover_color = self.hover_colors[i]
                button = Button(difficulty, button_rect, self.main_font, hover_color, "#ffffff")
                
            else:
                button = Button(difficulty, button_rect, self.main_font, color, "#ffffff")

            if i == self.difficulty_index:
                border_rect = button_rect.inflate(6, 6)
                pygame.draw.rect(screen, "#ffffff", border_rect, 1)

            button.draw(screen)
            self.rects.append((button_rect, difficulty))

        # Back
        back_rect = pygame.Rect((SCREEN_WIDTH // 2) - 100, 525, 200, 45)

        # Hover check
        mouse_pos = pygame.mouse.get_pos()
        if back_rect.collidepoint(mouse_pos):
            back_button = Button("Back", back_rect, self.main_font, "darkred", "#ffffff")
            back_button.draw(screen)

        else:
            back_button = Button("Back", back_rect, self.main_font, "red", "#ffffff")

        back_button.draw(screen)
        self.rects.append((back_rect, "Back"))