from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    #    l = Line(Point(50, 50), Point(400, 400))
    #    win.draw_line(l, "black")
    x = Cell(60, 70, 200, 750, win)
    win.wait_for_close()


main()
