from PIL import Image
import numpy as np


class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    path = path[::-1]
    return path


def search(image, start, end):
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0
    end_height = image[end[0]][end[1]]

    yet_to_visit_list = []
    visited_list = []
    yet_to_visit_list.append(start_node)

    outer_iterations = 0
    max_iterations = (len(image) // 2) ** 10

    move = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 1), (-1, 0)]

    while len(yet_to_visit_list) > 0:
        outer_iterations += 1
        current_node = yet_to_visit_list[0]
        current_index = 0

        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        if outer_iterations > max_iterations:
            print("FAILURE")
            return return_path(current_node)

        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        if current_node == end_node:
            return return_path(current_node)

        children = []
        for new_position in move:
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            if (node_position[0] > (len(image) - 1) or
                    node_position[0] < 0 or
                    node_position[1] > (len(image[0]) - 1) or
                    node_position[1] < 0):
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            child.g = current_node.g + (((child.position[0] - current_node.position[0]) ** 2) +
                                        ((child.position[1] - current_node.position[1]) ** 2) +
                                        ((image[child.position[0]][child.position[1]] -
                                          image[current_node.position[0]][current_node.position[1]]) ** 2)) ** .5
            child.h = (((child.position[0] - end[0]) ** 2) +
                       ((child.position[1] - end[1]) ** 2) +
                       ((image[child.position[0]][child.position[1]] -
                         end_height) ** 2)) ** .5
            child.f = child.g + child.h

            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue

            yet_to_visit_list.append(child)
    print("exited loop")


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
    img = Image.new('RGB', (len(array[0]), len(array)), color='red')

    pixels = img.load()
    for i in range(img.size[0]):  # for every col:
        for j in range(img.size[1]):  # For every row
            color = array[j][i]
            pixels[i, j] = (color, color, color)

    img.save('pil_image.png')
    return img


def add_path(image, path):
    pixels = image.load()
    for pos in path:
        pixels[pos[1], pos[0]] = (min(pixels[pos[1], pos[0]][0] + 200, 255), max(pixels[pos[1], pos[0]][1] - 0, 0),
                                  max(pixels[pos[1], pos[0]][2] - 0, 0))
    image.save('pil_image.png')
    # image.show()


def main():
    # array = readfile("Colorado_844x480.dat")
    array = np.random.randint(0, 255, (25, 50), dtype=int)
    array = normalize_array(array)
    image = create_map(array)
    a_star_path = search(array, (0, 0), (len(array) - 1, len(array[0]) - 1))
    add_path(image, a_star_path)


if __name__ == "__main__":
    main()
