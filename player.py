import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADIUS,
)
from shot import Shot


class Player(CircleShape):
    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: int | float
    rotation: float

    def __init__(self, x: int | float, y: int | float, *groups):
        super().__init__(x, y, PLAYER_RADIUS, *groups)
        self.rotation = 0.0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), 2)

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position, SHOT_RADIUS, *self.groups())
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOT_SPEED
        shot.velocity = velocity
