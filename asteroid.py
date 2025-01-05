from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)

        spv1 = self.velocity.rotate(split_angle)
        spv2 = self.velocity.rotate(-split_angle)

        split_radius = self.radius - ASTEROID_MIN_RADIUS

        new1 = Asteroid(self.position.x, self.position.y, split_radius)
        new1.velocity = spv1 * 1.2
        new2 = Asteroid(self.position.x, self.position.y, split_radius)
        new2.velocity = spv2 * 1.2