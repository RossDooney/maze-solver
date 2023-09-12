from graphics import Window, Line, Point
from cells import Cell


def main():
    win = Window(800, 600)
    #    l = Line(Point(50, 50), Point(400, 400))
    #    win.draw_line(l, "black")
    cell = Cell(win)
    cell.draw(70, 70, 200, 200)
    win.wait_for_close()


main()
