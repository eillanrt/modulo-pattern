#!/usr/bin/env python
from PIL import Image, ImageDraw
import os


def formula(a, b):
    # Replace with your own formula
    own_formula = ((9 * a) - (5 * a)) + ((2 * b) - (3 * b))
    return own_formula % 5


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def get_table():
    my_nums = [i for i in range(1, 6)]  # numbers {1, 2, 3, 4, 5}
    table = []

    for i in my_nums:
        row = []
        for j in my_nums:
            val = formula(i, j)
            if val == 0 and val not in my_nums:
                val = 5

            row.append(val)
        table.append(row)

    print('your table')
    print(table)

    return table


def generate_image_pattern():
    grid_size = 5
    cell_size = 200
    output_size = grid_size * cell_size
    table = flatten_list(get_table())

    res = input('proceed? y/n : ')
    if res != 'y':
        return

    new_image = Image.new('RGB', (output_size, output_size))

    for i in range(grid_size):
        for j in range(grid_size):
            index = i * grid_size + j
            if index < 25:
                with Image.open(os.path.join('pics', f'{table[index]}.png')) as image:
                    print('OPENED: ' + f'{table[index]}.png')
                    image = image.resize((cell_size, cell_size))
                    new_image.paste(image, (j * cell_size, i * cell_size))
                    new_image.save('pattern.png')


def main():
    generate_image_pattern()


if __name__ == '__main__':
    main()
