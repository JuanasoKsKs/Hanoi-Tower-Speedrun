import pygame
from piece import Piece
from column import Column
from constants import *
#from main import pieces

class PlayGround(pygame.sprite.Sprite):
    def __init__(self, capacity):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #self.add(*self.containers)
        self.capacity = capacity
        self.first_column = Column(SCREEN_WIDTH/6 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9)
        self.second_column = Column(SCREEN_WIDTH/2 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9)
        self.third_column = Column(SCREEN_WIDTH*5/6 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9)
        self.first = []
        self.second = []
        self.third = []
        self.pivot = 0
        self.create_pieces()

    def create_pieces(self):
        for i in range(self.capacity, 0, -1):
            self.first.append(i)
        for i in self.first:
            width = (PIECE_MAX_WIDTH - PIECE_MIN_WIDTH) / (self.capacity - 1)  * (i - 1) + PIECE_MIN_WIDTH
            x = SCREEN_WIDTH/6 - width /2
            y = SCREEN_HEIGHT*0.9 - PIECE_HEIGHT * (self.capacity - i) * (1.5) - PIECE_HEIGHT * .2 
            piece = Piece(x, y, width, i)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            if self.pivot == 0 and len(self.first) > 0:
                self.pivot = self.first.pop()
                print(self.pivot)
                print(self.first)
                for piece in pieces:
                    if piece.size == self.pivot:
                        piece.position.y = COLUMN_HEIGHT * 0.25



