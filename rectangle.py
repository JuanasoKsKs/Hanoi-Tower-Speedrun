import pygame

class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.position = pygame.Vector2(x, y)
        self.width = width
        self.height = height

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__(self) 

    def points(self):
        x1 = self.position
        x2 = self.position + pygame.Vector2(self.width, 0)
        y1 = self.position - pygame.Vector2(0, self.height)
        y2 = self.position + pygame.Vector2(self.width, 0) - pygame.Vector2(0, self.height)
        return [x1, x2, y2, y1]

    def draw(self, screen):
        #subclasses overwrite
        pass