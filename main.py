from typing import Any
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2.0
    y = SCREEN_HEIGHT / 2
    updatable: pygame.sprite.Group[Any] = pygame.sprite.Group()
    drawable: pygame.sprite.Group[Any] = pygame.sprite.Group()
    Player(x, y, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        updatable.update(dt)
        drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
