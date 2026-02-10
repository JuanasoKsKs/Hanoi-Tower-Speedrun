import pygame
from rectangle import RectangleShape
from constants import *

class Color():
    primero = (255, 255, 0)
    segundo = (51, 255, 0)
    tercero = (0, 255, 255)
    cuarto = (0, 0, 255)
    quinto = (120, 0, 250)
    sexto = (255, 0, 153)
    septimo = (255, 0, 0)
    octavo = (255, 255, 0)
    noveno = (51, 255, 0)
    decimo = (0, 150, 0)

class Piece(RectangleShape):
    def __init__(self, x, y, width, size):
        super().__init__(x, y, width, PIECE_HEIGHT)
        self.size = size

    def draw(self, screen):
        pygame.draw.polygon(screen, self.get_color(), self.points(), 0)

    def get_color(self):
        match self.size:
            case 1:
                return Color.primero
            case 2:
                return Color.segundo
            case 3:
                return Color.tercero
            case 4:
                return Color.cuarto
            case 5:
                return Color.quinto
            case 6:
                return Color.sexto
            case 7:
                return Color.septimo
            case 8:
                return Color.octavo
            case 9:
                return Color.noveno
            case 10:
                return Color.decimo
            case _:
                return "black"
            



    