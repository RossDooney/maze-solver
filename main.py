from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    #    l = Line(Point(50, 50), Point(400, 400))
    #    win.draw_line(l, "black")
    x = Cell([True, True, True, True], 50, 50, 200, 200, win)
    win.wait_for_close()


main()
