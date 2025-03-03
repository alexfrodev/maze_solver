from graphics import Point, Line


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):

        half_x = (self._x1 + self._x2) // 2
        half_y = (self._y1 + self._y2) // 2

        cell_half_x = (to_cell._x1 + to_cell._x2) // 2
        cell_half_y = (to_cell._y1 + to_cell._y2) // 2

        line = Line(
            Point(half_x, half_y),
            Point(cell_half_x, cell_half_y)
            )

        if undo == False:
            self._win.draw_line(line, fill_color="red")
        else:
            self._win.draw_line(line, fill_color="gray")

