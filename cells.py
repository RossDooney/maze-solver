from graphics import Window, Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        # possible better to use a list for this? self.has_walls = [False, False, False, False] if multiple walls may need to be removed
        # top right
        self._x1 = None
        self._y1 = None
        # top left
        self._x2 = None
        self._y2 = None
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_top_wall == True:
            self._win.draw_line(top_wall, "black")
        else:
            self._win.draw_line(top_wall, "White")
        if self.has_bottom_wall == True:
            self._win.draw_line(bottom_wall, "black")
        else:
            self._win.draw_line(bottom_wall, "White")
        if self.has_right_wall == True:
            self._win.draw_line(right_wall, "black")
        else:
            self._win.draw_line(right_wall, "White")
        if self.has_left_wall == True:
            self._win.draw_line(left_wall, "black")
        else:
            self._win.draw_line(left_wall, "White")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        middle_self_x = (self._x1 + self._x2) / 2
        middle_self_y = (self._y1 + self._y2) / 2
        middle_to_cell_x = (to_cell._x1 + to_cell._x2) / 2
        middle_to_cell_y = (to_cell._y1 + to_cell._y2) / 2

        middle_self_to_cell = Line(
            Point(middle_self_x, middle_self_y),
            Point(middle_to_cell_x, middle_to_cell_y),
        )
        line_color = "red"

        if undo:
            line_color = "grey"

        self._win.draw_line(middle_self_to_cell, line_color)
