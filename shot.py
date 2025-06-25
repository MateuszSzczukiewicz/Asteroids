import pygame

from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, position: pygame.Vector2, radius: int, *groups):
        super().__init__(position.x, position.y, radius, *groups)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius)

    def update(self, dt: float):
        self.position += self.velocity * dt
