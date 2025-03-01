from graphics import Window, Line, Point


def main():
    #Create a window
    win = Window(1200, 1000)

    #Define points
    p1 = Point(10,10)
    p2 = Point(300,300)

    #Create a line between points
    line = Line(p1, p2)
    #Draw line in canvas
    win.draw_line(line, "black")
    #Start app loop
    win.wait_for_close()


main()
