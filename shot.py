import pygame
from circleshape import *
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
import random
from Asteroid import Asteroid

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, radius=SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH or self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            self.should_delete = True
        else:
            self.should_delete = False
