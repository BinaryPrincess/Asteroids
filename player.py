from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
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

    def move(self, dt, direction=1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_position = self.position + forward * PLAYER_SPEED * dt * direction

        screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        if screen_rect.collidepoint(new_position.x, new_position.y):
            self.position = new_position


    def update(self, dt):
        keys = pygame.key.get_pressed()

        rotation_input = 0
        movement_input = 0

        if keys[pygame.K_a]: rotation_input -= 1
        if keys[pygame.K_d]: rotation_input += 1
        if keys[pygame.K_w]: movement_input += 1
        if keys[pygame.K_s]: movement_input -= 1

        if rotation_input != 0:
            self.rotate(dt, rotation_input)
        if movement_input != 0:
            self.move(dt, movement_input)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

