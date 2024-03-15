from time import time

import drawsvg as svg
from tqdm import *

import customobject as custom

print('Choose land type: (1)Square (2)Rectangle: ', end='')
option = int(input())
switch_1 = {1: lambda a: 'square', 2: lambda a: 'rectangle'}
land_type = switch_1[option](0)

# get size of land
if option == 1:
    print('enter land side length (mult by 10):', end=' ')
    width = int(input()) * 10
    height = width
    surface = height ** 2
# elif option == 2:
#     print('enter land width (mult by 10):', end=' ')
#     width = int(input())*10
#     print('enter land height (mult by 10):', end=' ')
#     height = int(input())*10
#     surface = width * height
else:
    raise ValueError("Not Implemented")

# get the numbers of entry
print('Input entry number: ', end='')
option = int(input())
switch_2 = {1: lambda a: 1, 2: lambda a: 2}
entry = switch_2[option](0)

# get the numbers of entry
print('Input path width(type) (1)3.5m (2)5.5m: ', end='')
option = int(input())
switch_3 = {1: lambda a: 3.5, 2: lambda a: 5.5}
path = switch_3[option](0)

# print datas
print(f'The land size is: {str(width)}*{str(height)}')
print(f'The surface of land is: {surface}')
s_time = time()

# create image
drawObj = svg.Drawing(width, height)

# define constants
c = custom.Constants(path=path)
grid_count = 0

# draw base for unused space
r = svg.Rectangle(0, 0, width=width, height=height, fill=c.color_unused, stroke=c.stroke,
                  stroke_width=c.stroke_width)
drawObj.append(r)

# drawing x grid on right side
grid_seq_1 = 0
for i in trange(int(height/c.grid_x_height)):
    r = custom.ParkingGrid(x=width - c.grid_x_width, y=grid_seq_1, width=c.grid_x_width, height=c.grid_x_height)
    drawObj.append(r)
    grid_seq_1 = grid_seq_1 + c.grid_x_height
    grid_count += 1

# drawing y grid on left side if necessary
grid_seq_2 = 0
grid_seq_3 = (width - c.grid_y_height + c.path_width) % c.grid_y_width
path_y_axis = c.grid_y_height
if height > 10 and width > 10:
    for i in trange(int(height/c.grid_y_height + c.path_width)):
        for j in range(int((width - c.grid_y_height + c.path_width) / c.grid_y_width)):
            r = custom.ParkingGrid(x=grid_seq_3, y=grid_seq_2, width=c.grid_y_width, height=c.grid_y_height)
            drawObj.append(r)
            grid_seq_3 += c.grid_y_width
            grid_count += 1
        r = svg.Rectangle(x=0, y=path_y_axis, height=c.path_width, width=width - 9, fill=c.color_path,
                          stroke=c.stroke, stroke_width=c.stroke_width)
        drawObj.append(r)
        grid_seq_3 = (width - c.grid_y_height + c.path_width) % c.grid_y_width
        grid_seq_2 += c.grid_y_height + c.path_width
        path_y_axis += c.grid_y_height + c.path_width

# draw auxiliary grid to fill space
grid_seq_4 = 0
if height % c.grid_y_height + c.path_width > c.grid_y_height:
    for i in trange(int((width - c.grid_y_height + c.path_width)/c.grid_y_width)):
        r = custom.ParkingGrid(x=width - (11.5 + grid_seq_4 * c.grid_y_width), y=path_y_axis - c.grid_y_width,
                               height=c.grid_y_height, width=c.grid_y_width)
        drawObj.append(r)
        grid_seq_4 += 1
elif height % c.grid_y_height + c.path_width > c.grid_x_height:
    for i in trange(int((width - c.grid_y_height + c.path_width)/c.grid_x_width)):
        r = custom.ParkingGrid(x=width - (14.5 + grid_seq_4 * c.grid_x_width), y=path_y_axis - c.grid_y_width,
                               height=c.grid_x_height, width=c.grid_x_width)
        drawObj.append(r)
        grid_seq_4 += 1

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
    if entry > 1:
        r = svg.Rectangle(x=width - c.grid_x_width - c.path_width, y=height - 1, width=c.path_width, height=1,
                      fill=c.color_entry, stroke=c.stroke, stroke_width=c.stroke_width)
    drawObj.append(r)
    drawObj.save_svg("10x10.svg")
    print(f'Grid Counts: {grid_count}')
elif width >= 10 and height >= 10:
    r = svg.Rectangle(x=0, y=5.5, width=1, height=c.path_width, fill=c.color_entry,
                      stroke=c.stroke, stroke_width=c.stroke_width)
    drawObj.append(r)
    if entry > 1:
        r = svg.Rectangle(x=0, y=height - (height % 9) - 3.5, width=1, height=c.path_width, fill=c.color_entry,
                      stroke=c.stroke, stroke_width=c.stroke_width)
    drawObj.append(r)
    drawObj.save_svg(f'{width}x{height}.svg')
    print(f'Grid Count: {grid_count}')

print(f'Spends {time() - s_time} seconds.')
