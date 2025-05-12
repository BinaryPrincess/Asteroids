from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
from circleshape import CircleShape
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.player_shoot_cooldown = 0

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

    def shoot(self):
        if self.player_shoot_cooldown > 0:
            return
        self.player_shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        bullet_direction = pygame.math.Vector2(0, 1).rotate(self.rotation)
        bullet_velocity = bullet_direction * PLAYER_SHOOT_SPEED
        Shot(self.position.copy(), bullet_velocity)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.player_shoot_cooldown = max(0, self.player_shoot_cooldown - dt)

        rotation_input = 0
        movement_input = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]: rotation_input -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: rotation_input += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]: movement_input += 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: movement_input -= 1
        if keys[pygame.K_SPACE]: self.shoot()
        
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
    