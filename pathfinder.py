from PIL import Image, ImageDraw
import numpy as np


def print_two_d_array(item):
    for num in range(len(item)):
        print(item[num])


def normalize_array(array):
    min_num = 9223372036854775807
    max_num = -9223372036854775807
    for line in array:
        for num in line:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
    max_num = max_num - min_num
    for line_num in range(len(array)):
        for i in range(len(array[line_num])):
            array[line_num][i] = (255 * (array[line_num][i] - min_num)) / max_num
            # if 200 <= line_num <= 201:
            #     array[line_num][i] = -10
    return array


def readfile(file_name):
    file = open(file_name, "r")
    array = []
    for x in file:
        line = x.split()
        int_line = []
        for num in range(len(line)):
            item = int(line[num])
            int_line.append(item)
        array.append(int_line)
    return np.array(array)


def create_map(array):
    img = Image.new('RGB', (len(array), len(array[0])), color='red')

    pixels = img.load()
    for i in range(img.size[0]):  # for every col:
        for j in range(img.size[1]):  # For every row
            color = array[i][j]
            pixels[i, j] = (color, color, color)

    img.save('pil_image.png')
    img.show(title="Image3")


def main():
    array = readfile("Colorado_480x480.dat")
    array = normalize_array(array)
    create_map(array)


if __name__ == "__main__":
    main()
