from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(self, walls, x1, y1, x2, y2, win):
        #        self.has_left_wall = False
        #        self.has_right_wall = False
        #        self.has_top_wall = False
        #        self.has_bottom_wall = False
        self.has_wall = walls
        self._win = win
        # possible better to use a list for this? self.has_walls = [False, False, False, False]
        # top right
        self._x1 = x1
        self._y1 = y1
        # top left
        self._x2 = x2
        self._y2 = y2
        print(self.has_wall)
        if self.has_wall[0] == True:
            top_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(top_wall, "black")
        if self.has_wall[1] == True:
            bottom_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(bottom_wall, "black")
        if self.has_wall[2] == True:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, "black")
        if self.has_wall[3] == True:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall, "black")


#       l = Line(Point(self._x1, self._y1), Point(self._x2, self._y2))
#       self._win.draw_line(l, "black")
