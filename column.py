import pygame
from rectangle import RectangleShape

class Column(RectangleShape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.points(), 0)


    