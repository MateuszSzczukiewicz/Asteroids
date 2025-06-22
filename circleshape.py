from typing import Any, ClassVar
import pygame


class CircleShape(pygame.sprite.Sprite):
    containers: ClassVar[pygame.sprite.AbstractGroup[Any]]

    def __init__(
        self,
        x: int | float,
        y: int | float,
        radius: int | float,
        *groups: pygame.sprite.AbstractGroup[Any]
    ):
        super().__init__(*groups)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        pass

    def update(self, dt: float):
        pass
