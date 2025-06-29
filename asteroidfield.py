from typing import Callable
import pygame
import random
from asteroid import Asteroid
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class AsteroidField(pygame.sprite.Sprite):
    spawn_timer: float
    EdgeDefinition = tuple[pygame.Vector2, Callable[[float], pygame.Vector2]]

    edges: list[EdgeDefinition] = [
        (
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ),
        (
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ),
        (
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ),
        (
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ),
    ]

    def __init__(
        self,
        target_asteroids_group,
        target_drawable_group,
        *groups_for_spawner,
    ):
        super().__init__(*groups_for_spawner)

        self.asteroids_group = target_asteroids_group
        self.drawable_group = target_drawable_group
        self.spawn_timer = 0.0

    def spawn(self, radius: int, position: pygame.Vector2, velocity: pygame.Vector2):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

        asteroid.add(self.asteroids_group, self.drawable_group, *self.groups())

    def update(self, dt: float):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
