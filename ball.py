import pygame
import random
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Ball:
    def __init__(self):
        self.color = ((255, 255, 255))
        self.radius = 15

        self.texture = pygame.image.load("assets/images/ball.png").convert_alpha()
        self.texture = pygame.transform.smoothscale(self.texture, (self.radius * 2, self.radius * 2))

        self.reset()


    def reset(self):
        self.x_pos = SCREEN_WIDTH // 2
        self.y_pos = SCREEN_HEIGHT // 2

        self.speed = 4
        self.acceleration = 1.025
        self.starting_angle = random.randint(5, 30)
        self.max_bounce_angle = 45
        self.x_direction = random.choice([-1, 1])
        self.y_direction = random.choice([-1, 1])

        self.starting_angle_radians = math.radians(self.starting_angle)

        self.x_vel = self.x_direction * self.speed * math.cos(self.starting_angle_radians)
        self.y_vel = self.y_direction * self.speed * math.sin(self.starting_angle_radians)


    def handle_wall_collisions(self):
        # Top wall
        if self.y_pos - self.radius <= 0:
            self.y_pos = self.radius
            self.y_vel *= -1

        # Bottom wall
        elif self.y_pos + self.radius >= SCREEN_HEIGHT:
            self.y_pos = SCREEN_HEIGHT - self.radius
            self.y_vel *= -1
        

    def check_for_round_over(self):
        # Left wall
        if self.x_pos + self.radius <= 0:
            return True, "Left"
        
        # Right wall
        elif self.x_pos + self.radius >= SCREEN_WIDTH:
            return True, "Right"
        
        else:
            return False, "None"


    def handle_paddle_collisions(self, paddle_rect):
        # Find where ball hit relative to paddle center
        paddle_center_y = paddle_rect.y + paddle_rect.height / 2
        relative_intersect_y = self.y_pos - paddle_center_y
        normalized_intersect_y = relative_intersect_y / (paddle_rect.height / 2)

        # Determine bounce angle
        bounce_angle = normalized_intersect_y * self.max_bounce_angle
        angle_rad = math.radians(bounce_angle)

        # Determine horizontal direction (left/right)
        if paddle_rect.x < SCREEN_WIDTH / 2:
            direction = 1  # left paddle → bounce right
        else:
            direction = -1  # right paddle → bounce left

        # Increase speed after each hit
        self.speed *= self.acceleration

        # Recalculate velocity
        self.x_vel = direction * self.speed * math.cos(angle_rad)
        self.y_vel = self.speed * math.sin(angle_rad)


    def update(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

        self.handle_wall_collisions()


    def draw(self, screen):
        self.ball_rect = screen.blit(self.texture, (self.x_pos - self.radius, self.y_pos - self.radius))