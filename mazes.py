from cells import Cell
from graphics import Window, Line, Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        x_1 = 50
        x_2 = 100
        y_1 = 50
        y_2 = 100
        for i in range(self._num_rows):
            cell = Cell(self._win)
            self._cells.append(cell)

        for i in range(len(self._cells)):
            self._cells[i].draw(x_1, y_1, x_2, y_2)
            x_1 += 50
            x_2 += 50

    def _draw_cell(self, i, j):
        return

    def _animate(self):
        return
