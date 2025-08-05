import pygame
from paddles import Paddles
from ball import Ball
from text import ScoreText, PauseText, ResultsText
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Game:
    def __init__(self, mode, difficulty):
        self.bg = pygame.image.load("assets/images/background.png").convert()
        self.bg = pygame.transform.smoothscale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.mode = mode
        self.difficulty = difficulty

        self.paddles = Paddles()
        self.ball = Ball()
        self.apply_options()

        self.score_text = ScoreText()
        self.pause_text = PauseText()
        self.results_text = ResultsText()

        self.score1 = 0
        self.score2 = 0
        self.max_score = 11
        self.game_over = False
        self.game_over_time = None

        self.bounce_sound = pygame.mixer.Sound("assets/sounds/bounce.wav")
        self.score_sound = pygame.mixer.Sound("assets/sounds/score.wav")
        
        self.bounce_sound.set_volume(0.5)
        self.score_sound.set_volume(0.5)

        self.start_timer()
        self.in_round_pause = True


    def apply_options(self):
        # Apply mode settings
        if self.mode == 0:
            self.paddles.current_mode = "vsPlayer"
        elif self.mode == 1:
            self.paddles.current_mode = "vsBot"

        # Apply difficulty settings
        if self.difficulty == 0:
            self.paddles.bot_speed = 6
        
        elif self.difficulty == 1:
            self.paddles.bot_speed = 8

        elif self.difficulty == 2:
            self.paddles.bot_speed = 10

        elif self.difficulty == 3:
            self.paddles.bot_speed = 12


    def handle_paddle_and_ball_collisions(self):
        collision = False

        # Paddle 1
        if self.ball.ball_rect.colliderect(self.paddles.paddle1_rect):
            self.ball.handle_paddle_collisions(self.paddles.paddle1_rect)
            collision = True

        # Paddle 2
        if self.ball.ball_rect.colliderect(self.paddles.paddle2_rect):
            self.ball.handle_paddle_collisions(self.paddles.paddle2_rect)
            collision = True

        if collision and not self.last_collision:
            self.bounce_sound.play()

        self.last_collision = collision


    def start_timer(self):
        self.round_pause_start = pygame.time.get_ticks()
        self.in_round_pause = True


    def handle_round_over(self):
        self.round_over, side = self.ball.check_for_round_over()
        
        if self.round_over:
            self.round_over = False

            if side == "Left":
                self.score2 += 1
                self.score_sound.play()

            elif side == "Right":
                self.score1 += 1
                self.score_sound.play()

            self.score_text.set_score(self.score1, self.score2)

            self.ball.reset()
            self.paddles.reset()

            self.start_timer()


    def check_for_game_over(self):
        if self.score1 == self.max_score or self.score2 == self.max_score:
            self.game_over = True

    
    def draw_results(self):
        if self.paddles.current_mode == "vsBot":
            print(self.score1, self.score2, self.max_score)
            if self.score1 == self.max_score:
                result_id = 0
            if self.score2 == self.max_score:
                result_id = 1

        elif self.paddles.current_mode == "vsPlayer":
            if self.score1 == self.max_score:
                result_id = 2
            if self.score2 == self.max_score:
                result_id = 3


        self.results_text.set_results_id(result_id)


    def handle_game_over(self):
        if self.game_over:
            if self.game_over_time is None:
                # Record when game over started
                self.game_over_time = pygame.time.get_ticks()

                # Reset ball and paddles
                self.ball.reset()
                self.paddles.reset()

                # Draw results
                self.draw_results()

                # Reset scores
                self.score1 = 0
                self.score2 = 0

                # Reset text
                self.score_text.set_score(self.score1, self.score2)


    def is_post_game_done(self):
        if self.game_over_time is not None:
            return (pygame.time.get_ticks() - self.game_over_time) >= 2000
        return False
                

    def update(self):
        if not self.game_over:
            self.check_for_game_over()

            # Check if we're in the 3-second pause
            if self.in_round_pause:
                now = pygame.time.get_ticks()
                elapsed = (now - self.round_pause_start) // 1000
                remaining = 3 - elapsed

                self.pause_text.set_timer(remaining)

                if remaining <= -1:
                    self.in_round_pause = False
        
            else:
                self.ball.update()
                self.paddles.update(self.ball.y_pos)

                self.handle_paddle_and_ball_collisions()
                self.handle_round_over()

        else:
            self.handle_game_over()


    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.bg, (0, 0))

        if not self.game_over:
            self.paddles.draw(screen)
            self.ball.draw(screen)

            self.score_text.draw(screen)

            if self.in_round_pause:
                self.pause_text.draw(screen)

        if self.game_over:
            self.results_text.draw(screen)