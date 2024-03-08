import drawsvg as svg
import svgApplet as SvgX
from tqdm import *
from time import time

# get size of land
print('enter land side length (mult by 10):', end=' ')
width = int(input())*10
height = width
# print('enter land height (mult by 10):', end=' ')
# height = int(input())*10
print(f'The land size is: {str(width)}*{str(height)}')
s_time = time()

# create image
drawObj = svg.Drawing(width, height)

# define constants
c = SvgX.Constants()
grid_count = 0

# draw base for unused space
r = svg.Rectangle(0, 0, width=width, height=height, fill=c.color_unused, stroke=c.stroke,
                  stroke_width=c.stroke_width)
drawObj.append(r)

# drawing x grid on right side
grid_seq_1 = 0
print('Draw x grid')
for i in trange(int(height/10*4)):
    r = SvgX.ParkingGrid(x=width - c.grid_x_width, y=grid_seq_1, width=c.grid_x_width, height=c.grid_x_height)
    drawObj.append(r)
    grid_seq_1 = grid_seq_1 + c.grid_x_height
    grid_count += 1

# drawing y grid on left side if necessary
grid_seq_2 = 0
grid_seq_3 = (width - 9) % 2.5
path_y_axis = 5.5
if height > 10 and width > 10:
    for i in trange(int(height/9)):
        for j in range(int((width - 8) / 2.5)):
            r = SvgX.ParkingGrid(x=grid_seq_3, y=grid_seq_2, width=c.grid_y_width, height=c.grid_y_height)
            drawObj.append(r)
            grid_seq_3 += 2.5
            grid_count += 1
        r = svg.Rectangle(x=0, y=path_y_axis, height=c.path_width, width=width - 9, fill=c.color_path, stroke=c.stroke, stroke_width=c.stroke_width)
        drawObj.append(r)
        grid_seq_3 = (width - 9) % 2.5
        grid_seq_2 += 9
        path_y_axis += 9

# draw the path
r = svg.Rectangle(x=width - c.grid_x_width - c.path_width, y=0, width=c.path_width, height=height, fill=c.color_path,
                  stroke=c.stroke, stroke_width=c.stroke_width)
drawObj.append(r)

# draw entry and save image
entry_seq_1 = 0
if width == 10 and height == 10:
    r = svg.Rectangle(x=width - c.grid_x_width - c.path_width, y=0, width=c.path_width, height=1, fill=c.color_entry,
                      stroke=c.stroke, stroke_width=c.stroke_width)
    drawObj.append(r)
    r = svg.Rectangle(x=width - c.grid_x_width - c.path_width, y=height - 1, width=c.path_width, height=1, fill=c.color_entry,
                      stroke=c.stroke, stroke_width=c.stroke_width)
    drawObj.append(r)
    drawObj.save_svg("10x10.svg")
    print(f'Grid Counts: {grid_count}')
elif width > 10 and height > 10:
    r = svg.Rectangle(x=0, y=5.5, width=1, height=c.path_width, fill=c.color_entry,
                      stroke=c.stroke, stroke_width=c.stroke_width)
    drawObj.append(r)
    r = svg.Rectangle(x=0, y=height - (height % 9) - 3.5, width=1, height=c.path_width, fill=c.color_entry,
                      stroke=c.stroke, stroke_width=c.stroke_width)
    drawObj.append(r)
    drawObj.save_svg(f'{width}x{height}.svg')
    print(f'Grid Count: {grid_count}')

print(f'Spends {time() - s_time} seconds.')
