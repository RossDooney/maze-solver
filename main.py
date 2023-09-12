from graphics import Window, Line, Point
from cells import Cell


def main():
    win = Window(800, 600)
    #    l = Line(Point(50, 50), Point(400, 400))
    #    win.draw_line(l, "black")
    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(50, 50, 100, 100)

    win.wait_for_close()


main()
