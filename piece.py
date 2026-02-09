import pygame
from rectangle import RectangleShape
from constants import *

class Piece(RectangleShape):
    def __init__(self, x, y, width, size):
        super().__init__(x, y, width, PIECE_HEIGHT)
        self.size = size

    def draw(self, screen):
        pygame.draw.polygon(screen, "lightblue", self.points(), 0)


    