import pygame
from rectangle import RectangleShape
from constants import *

class Column(RectangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, COLUMN_WIDTH, COLUMN_HEIGHT)

    def draw(self, screen):
        pygame.draw.polygon(screen, (179, 141, 75), self.points(), 0)


    