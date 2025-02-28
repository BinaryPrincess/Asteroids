from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt, direction=1):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        print(f"Update called, dt={dt}, rotation={self.rotation}")

        if keys[pygame.K_a]:
            print("A key pressed")
            self.rotate(dt, -1)
        if keys[pygame.K_d]:
            print("D key pressed")
            self.rotate(dt, 1)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

