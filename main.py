from graphics import Window, Line, Point
from cell import Cell


def main():
    #Create a window
    win = Window(1200, 1000)

    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(350, 50, 400 ,100)


    #Start window loop
    win.wait_for_close()


main()
