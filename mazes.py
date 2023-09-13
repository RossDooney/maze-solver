import time
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
        y_1 = 50
        for i in range(self._num_cols):
            cells_col = []
            for j in range(self._num_rows):
                cells_col.append(Cell(self._win))
            self._cells.append(cells_col)

        for j in range(self._num_cols):
            for i in range(self._num_rows):
                self._draw_cell(i, j)
                # self._cells[j].draw(
                #     x_1, y_1, x_1 + self._cell_size_x, y_1 + self._cell_size_y
                # )
                x_1 += self._cell_size_x
            y_1 += self._cell_size_y

    def _draw_cell(self, i, j):
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
