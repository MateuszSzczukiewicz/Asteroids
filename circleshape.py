import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int | float, y: int | float, radius: int | float, *groups):
        super().__init__(*groups)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        pass

    def update(self, dt: float):
        pass

    def check_collision(self, circle: "CircleShape") -> bool:
        distance = self.position.distance_to(circle.position)
        return distance < self.radius + circle.radius
