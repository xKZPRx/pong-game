import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Paddles:
    def __init__(self):
        self.width = 25
        self.height = 100

        self.texture = pygame.image.load("assets/images/paddle.png").convert()
        self.texture = pygame.transform.smoothscale(self.texture, (self.width, self.height))

        self.current_mode = "vsBot"
        self.player_speed = 8
        self.bot_speed = 8

        self.reset()


    def reset(self):
        # First paddle
        self.x_pos1 = 0
        self.y_pos1 = (SCREEN_HEIGHT // 2) - (0.5 * self.height)

        # Second paddle
        self.x_pos2 = SCREEN_WIDTH - self.width
        self.y_pos2 = (SCREEN_HEIGHT // 2) - (0.5 * self.height)


    def handle_bot_movement(self, ball_y):
        target_y = ball_y - self.height / 2
        distance = target_y - self.y_pos2

        # Limit the movement by bot_speed
        if abs(distance) < self.bot_speed:
            self.y_pos2 = target_y
        else:
            self.y_pos2 += self.bot_speed if distance > 0 else -self.bot_speed


    def handle_wall_collision(self):
        # First paddle
        if self.y_pos1 <= 0:
            self.y_pos1 += self.player_speed
        if self.y_pos1 >= (SCREEN_HEIGHT - self.height):
            self.y_pos1 -= self.player_speed

        # Second paddle
        if self.y_pos2 <= 0:
            self.y_pos2 += self.player_speed
        if self.y_pos2 >= (SCREEN_HEIGHT - self.height):
            self.y_pos2 -= self.player_speed


    def update(self, ball_y):
        keys = pygame.key.get_pressed()
        self.handle_wall_collision()

        # First paddle
        if keys[pygame.K_w]:
            self.y_pos1 -= self.player_speed
        if keys[pygame.K_s]:
            self.y_pos1 += self.player_speed

        if self.current_mode == "vsPlayer":
            # Second paddle
            if keys[pygame.K_UP]:
                self.y_pos2 -= self.player_speed
            if keys[pygame.K_DOWN]:
                self.y_pos2 += self.player_speed

        else:
            self.handle_bot_movement(ball_y)
            # Second paddle
            if keys[pygame.K_UP]:
                self.y_pos1 -= self.player_speed
            if keys[pygame.K_DOWN]:
                self.y_pos1 += self.player_speed


    def draw(self, screen):
        self.paddle1_rect = screen.blit(self.texture, (self.x_pos1, self.y_pos1, self.width, self.height)) # First paddle
        self.paddle2_rect = screen.blit(self.texture, (self.x_pos2, self.y_pos2, self.width, self.height)) # Second paddle