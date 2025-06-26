from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    position: pygame.Vector2

    def __init__(self, x: int | float, y: int | float, radius: int | float, *groups):
        super().__init__(x, y, radius, *groups)
        self.width = 2

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, pygame.Color("white"), self.position, self.radius, self.width
        )

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            randomAngle = random.uniform(20, 50)

            firstVector = self.velocity.rotate(randomAngle)
            secondVector = self.velocity.rotate(-randomAngle)

            newRadius = self.radius - ASTEROID_MIN_RADIUS

            firstAsteroid = Asteroid(
                self.position.x, self.position.y, newRadius, *self.groups()
            )
            secondAsteroid = Asteroid(
                self.position.x, self.position.y, newRadius, *self.groups()
            )

            firstAsteroid.velocity = firstVector * 1.2
            secondAsteroid.velocity = secondVector * 1.2

            self.kill()
