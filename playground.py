import pygame
from piece import Piece
from column import Column
from constants import *
#from main import pieces

class PlayGround(pygame.sprite.Sprite):
    def __init__(self, capacity, pieces, game):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.pieces = pieces
        self.capacity = capacity
        self.moves = 0
        self.time = 0.0
        self.first_column = Column(SCREEN_WIDTH/6 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9)
        self.second_column = Column(SCREEN_WIDTH/2 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9)
        self.third_column = Column(SCREEN_WIDTH*5/6 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9)
        self.first = []
        self.second = []
        self.third = []
        self.lock_one = False
        self.lock_two = False
        self.lock_three = False
        self.pivot = 0
        self.create_pieces()
        self.game = game

    def create_pieces(self):
        self.first = []
        self.second = []
        self.third = []
        for victim in self.pieces:
            victim.kill()

        for i in range(self.capacity, 0, -1):
            self.first.append(i)
        for i in self.first:
            width = (PIECE_MAX_WIDTH - PIECE_MIN_WIDTH) / (self.capacity - 1)  * (i - 1) + PIECE_MIN_WIDTH
            x = SCREEN_WIDTH/6 - width /2
            y = self.get_y(self.first.index(i))
            piece = Piece(x, y, width, i)
    
    def update(self):
        self.game.started = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and self.lock_one == False:
            if self.pivot == 0:
                if len(self.first) > 0:
                    self.moves += 1
                    self.pivot = self.first.pop()
                    for piece in self.pieces:
                        if piece.size == self.pivot:
                            piece.position.y = SCREEN_HEIGHT * 0.25
            elif len(self.first) == 0 or self.first[-1] > self.pivot:
                self.first.append(self.pivot)
                for piece in self.pieces:
                    if piece.size == self.pivot:
                        y = self.get_y(self.first.index(self.pivot))
                        x = SCREEN_WIDTH/6 - piece.width/2
                        piece.position.y = y
                        piece.position.x = x
                self.pivot = 0
        if keys[pygame.K_2] and self.lock_two == False:
            if self.pivot == 0:
                if len(self.second) > 0:
                    self.moves += 1
                    self.pivot = self.second.pop()
                    for piece in self.pieces:
                        if piece.size == self.pivot:
                            piece.position.y = SCREEN_HEIGHT * 0.25
            elif len(self.second) == 0 or self.second[-1] > self.pivot:
                self.second.append(self.pivot)
                for piece in self.pieces:
                    if piece.size == self.pivot:
                        y = self.get_y(self.second.index(self.pivot))
                        x = SCREEN_WIDTH/2 - piece.width/2
                        piece.position.y = y
                        piece.position.x = x
                self.pivot = 0
        if keys[pygame.K_3] and self.lock_three == False:
            if self.pivot == 0:
                if len(self.third) > 0:
                    self.moves += 1
                    self.pivot = self.third.pop()
                    for piece in self.pieces:
                        if piece.size == self.pivot:
                            piece.position.y = SCREEN_HEIGHT * 0.25
            elif len(self.third) == 0 or self.third[-1] > self.pivot:
                self.third.append(self.pivot)
                for piece in self.pieces:
                    if piece.size == self.pivot:
                        y = self.get_y(self.third.index(self.pivot))
                        x = SCREEN_WIDTH*5/6 - piece.width/2
                        piece.position.y = y
                        piece.position.x = x
                self.pivot = 0
    
    def get_y(self, column):
        return SCREEN_HEIGHT*0.9 - PIECE_HEIGHT * column * (1.1) - PIECE_HEIGHT * .2



