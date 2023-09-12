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
        maze_height = self._win.height
        maze_width = self._win.width

    def _draw_cell(self, i, j):
        return

    def _animate(self):
        return
