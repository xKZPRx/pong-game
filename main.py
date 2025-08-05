""" Pong Game by Kacper Wawrzonkiewicz """
import pygame
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game import Game
from menu import Menu
from options import Options


class Pong:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.running = True
        self.state = "menu"
        self.mode_index = 1
        self.difficulty_index = 1

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong Game")

        self.clock = pygame.time.Clock()

        self.menu = Menu()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                quit(0)

            # Open menu in game
            if self.state == "game":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.state = "menu"

            # Menu controls
            if self.state == "menu":

                # Get selected menu option
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for option_rect, selected_option in self.menu.rects:
                        if option_rect.collidepoint(mouse_pos):

                            # Handle the selected option
                            if selected_option == "Play":
                                self.state = "game"
                                self.game = Game(self.mode_index, self.difficulty_index)

                            elif selected_option == "Options":
                                self.state = "options"
                                self.options = Options()

                                self.options.mode_index = self.mode_index
                                self.options.difficulty_index = self.difficulty_index

                            else:
                                self.running = False
                                pygame.quit()
                                quit(0)

            # Option controls
            if self.state == "options":

                # Get selected options option
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for option_rect, option in self.options.rects:
                        if option_rect.collidepoint(mouse_pos):
                            
                            # Handle the selected option
                            if option == "Back":
                                self.state = "menu"
                                self.menu = Menu()

                            if option == "vsPlayer":
                                self.mode_index = 0
                                self.options.mode_index = 0

                            if option == "vsBot":
                                self.mode_index = 1
                                self.options.mode_index = 1

                            if option == "Easy":
                                self.difficulty_index = 0
                                self.options.difficulty_index = 0

                            if option == "Medium":
                                self.difficulty_index = 1
                                self.options.difficulty_index = 1
                            
                            if option == "Hard":
                                self.difficulty_index = 2
                                self.options.difficulty_index = 2

                            if option == "Extreme":
                                self.difficulty_index = 3
                                self.options.difficulty_index = 3


    def run(self):
        while self.running:
            self.handle_events()
            
            if self.state == "menu":
                self.menu.draw(self.screen)

            if self.state == "game":
                self.game.draw(self.screen)
                self.game.update()

            if self.state == "game":
                if self.game.game_over and self.game.is_post_game_done():
                    self.state = "menu"

            if self.state == "options":
                self.options.draw(self.screen)

            self.clock.tick(FPS)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    os.system('cls')
    pong = Pong()
    pong.run()