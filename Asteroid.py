from circleshape import *
import pygame
from constants  import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid(CircleShape):
    def __init__(self, position, velocity, radius):
        super().__init__(position, velocity, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius or self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius:
            self.should_delete = True
        else:
            self.should_delete = False