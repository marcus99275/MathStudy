import drawsvg


class Constants(drawsvg.Rectangle):
    def __init__(self):
        super().__init__(x=0, y=0, width=0, height=0)

        self.color_unused = '#ff0000'
        self.color_grid = '#ffff00'
        self.color_path = '#00ffff'
        self.color_entry = '#ff00ff'
        self.stroke = '#000000'
        self.stroke_width = 0.2
        self.grid_x_width = 5.5
        self.grid_x_height = 2.5
        self.grid_y_width = 2.5
        self.grid_y_height = 5.5
        self.path_width = 3.5


class ParkingGrid(drawsvg.Rectangle):
    def __init__(self, x, y, width, height):
        c = Constants()
        super().__init__(x=x, y=y, width=width, height=height, fill=c.color_grid,
                         stroke=c.stroke, stroke_width=c.stroke_width)
