import pygame

from random import choice


class Cell:
    def __init__(self, x, y, thickness):
        self.x = x
        self.y = y
        self.thickness = thickness
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw(self, Surface):
        if self.walls['top']:
            pygame.draw.line(Surface, pygame.Color('blue'), (self.x, self.y), (self.x + 1, self.y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(Surface, pygame.Color('darkgreen'), (self.x + 1, self.y, (self.x + 1, self.y + 1), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(Surface, pygame.Color('darkgreen'), (self.x + 1, self.y + 1), (self.x, self.y + 1), self.thickness)
        if self.walls['left']:
            pygame.draw.line(Surface, pygame.Color('darkgreen'), (self.x, self.y + 1), (self.x, self.y), self.thickness)

    def check_cell(self, x, y, cols, rows):
        if self.x < 0 or self.x > cols - 1 or self.y < 0 or self.y > rows - 1:
            return False
        return True

    def check_neighbors(self, cols, rows):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, cols, rows)
        right = self.check_cell(self.x + 1, self.y, cols, rows)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows)
        left = self.check_cell(self.x - 1, self.y, cols, rows)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        if neighbors:
            return choice(neighbors)
        else:
            return False