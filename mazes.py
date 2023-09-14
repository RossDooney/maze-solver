import time
from cells import Cell
from graphics import Window, Line, Point
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_walls_r(0, 0)
        if seed:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            cells_col = []
            for j in range(self._num_rows):
                cells_col.append(Cell(self._win))
            self._cells.append(cells_col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

        self._break_exit_and_enterance(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_exit_and_enterance(self, i, j):
        self._cells[0][0].has_left_wall = False
        self._cells[i][j].has_right_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            new_index_list = []

            possible_directions = 0

            if i > 0 and not self._cells[i - 1][j].visited:
                new_index_list.append((i - 1, j))
                possible_directions += 1
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                new_index_list.append((i + 1, j))
                possible_directions += 1
            if j > 0 and not self._cells[i][j - 1].visited:
                new_index_list.append((i, j - 1))
                possible_directions += 1
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                new_index_list.append((i, j + 1))
                possible_directions += 1

            if possible_directions == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(possible_directions)
            next_index = new_index_list[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])
