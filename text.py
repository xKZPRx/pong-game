import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class ScoreText:
    def __init__(self):
        pygame.font.init()

        self.color = ((255, 255, 255))
        self.font = pygame.font.Font(None, 50)
        self.score1 = 0
        self.score2 = 0
        self.rendered_text = self.font.render(str(f"{self.score1} - {self.score2}"), True, self.color)
        self.update_render()


    def update_render(self):
        self.rendered_text = self.font.render(f"{self.score1} - {self.score2}", True, self.color)
        self.x = (SCREEN_WIDTH // 2) - (self.rendered_text.get_width() // 2)
        self.y = 10


    def set_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2
        self.update_render()


    def draw(self, screen):
        screen.blit(self.rendered_text, (self.x, self.y))


class PauseText:
    def __init__(self):
        pygame.font.init()

        self.color = ((255, 255, 255))
        self.font = pygame.font.Font(None, 100)
        self.timer = 3
        self.rendered_text = self.font.render(str(self.timer), True, self.color)
        self.update_render()


    def update_render(self):
        if self.timer == 0:
            self.rendered_text = self.font.render(str("Start!"), True, self.color)

        elif self.timer > 0:
            self.rendered_text = self.font.render(str(self.timer), True, self.color)

        self.x = (SCREEN_WIDTH // 2) - (self.rendered_text.get_width() // 2)
        self.y = 150


    def set_timer(self, remaining):
        self.timer = remaining
        self.update_render()


    def draw(self, screen):
        screen.blit(self.rendered_text, (self.x, self.y))


class ResultsText:
    def __init__(self):
        pygame.font.init()

        self.color = ((255, 255, 255))
        self.font = pygame.font.Font(None, 150)
        self.results = ["You win!", "You lose!", "Player 1 wins!", "Player 2 wins!"]
        self.results_id = 0
        self.rendered_text = self.font.render("No results!", True, self.color)
        self.update_render()


    def set_results_id(self, results_id):
        self.results_id = results_id
        self.update_render()


    def update_render(self):
        self.rendered_text = self.font.render(self.results[self.results_id], True, self.color)

        self.x = (SCREEN_WIDTH // 2) - (self.rendered_text.get_width() // 2)
        self.y = (SCREEN_HEIGHT // 2) - (self.rendered_text.get_height() // 2)


    def draw(self, screen):
        screen.blit(self.rendered_text, (self.x, self.y))