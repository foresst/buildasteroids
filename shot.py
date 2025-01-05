from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
         super().__init__(x, y, SHOT_RADIUS)
         self.color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt