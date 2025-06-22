from circleshape import CircleShape
import pygame


class Asteroid(CircleShape):
    position: pygame.Vector2

    def __init__(self, x: int | float, y: int | float, radius: int, *groups):
        super().__init__(x, y, radius, *groups)
        self.width = 2

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, pygame.Color("white"), self.position, self.radius, self.width
        )

    def update(self, dt: float):
        self.position += self.velocity * dt
