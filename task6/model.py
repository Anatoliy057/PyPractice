import functools
import json
import random
import math

from task6 import point


class Game:

    def __init__(self, size: int):
        if size < 4:
            raise ValueError('To small size')
        self._model = [[0 for j in range(size)] for i in range(size)]
        self._size = size
        self._max_cell = 0

    def load(self, model: list):
        self._size = len(model)
        self._model = model
        self._max_cell = 0
        for i in range(self._size):
            for j in range(self._size):
                self._max_cell = max(self._max_cell, model[i][j])

    def reset(self, size):
        self._model = [[0 for j in range(size)] for i in range(size)]
        self._size = size
        self._max_cell = 0
        self.spawn(3)


    def spawn(self, count: int) -> bool:
        size = self._size

        possible = Game.count_empty_cells(self._model, size)
        count = min(possible, count)

        limit = max(3, int(self._max_cell / 2))
        for i in range(count):
            cell = random.randint(1, limit)
            while True:
                x = random.randint(0, size-1)
                y = random.randint(0, size-1)
                if self._model[x][y] == 0:
                    self._model[x][y] = cell
                    self._max_cell = max(self._max_cell, cell)
                    break
        return True

    def is_over(self):
        for i in range(self._size):
            for j in range(self._size):
                if self._model[i][j] == 0:
                    return False
                if i > 0 and self._model[i][j] == self._model[i-1][j]:
                    return False
                if i < self._size - 1 and self._model[i][j] == self._model[i+1][j]:
                    return False
                if j > 0 and self._model[i][j] == self._model[i][j-1]:
                    return False
                if j < self._size - 1 and self._model[i][j] == self._model[i][j+1]:
                    return False
        return True

    def get_model(self):
        return self._model

    def move(self, p1: point, p2: point) -> bool:
        x1 = p1.get_x()
        y1 = p1.get_y()
        x2 = p2.get_x()
        y2 = p2.get_y()
        if (x1 != x2 and y1 != y2) or p1 == p2:
            return False
        cell1 = self._model[x1][y1]
        cell2 = self._model[x2][y2]
        if cell1 != cell2 and cell2 != 0:
            return False
        if x1 == x2:
            x = x1
            sign_function = functools.partial(math.copysign, 1)
            sign = int(sign_function(y2 - y1))
            for y in range(y1 + sign, y2, sign):
                if self._model[x][y] != 0:
                    return False
        elif y1 == y2:
            y = y1
            sign_function = functools.partial(math.copysign, 1)
            sign = int(sign_function(x2 - x1))
            for x in range(x1 + sign, x2, sign):
                if self._model[x][y] != 0:
                    return False
        self._model[x1][y1] = 0
        if cell2 > 0:
            self._model[x2][y2] = cell1 + 1
            self.spawn(1)
        else:
            self._model[x2][y2] = cell1
            self.spawn(2)
        self._max_cell = max(self._max_cell, self._model[x2][y2])
        return True

    def size(self):
        return self._size

    def max_cell(self):
        return self._max_cell

    @staticmethod
    def count_empty_cells(model: list, size: int) -> int:
        count = 0
        for i in range(size):
            for j in range(size):
                if model[i][j] == 0:
                    count += 1
        return count
