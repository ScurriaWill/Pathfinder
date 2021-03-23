import sys


def print_two_d_array(item):
    for num in range(len(item)):
        print(item[num])


def normalize_array(array):
    min_num = sys.maxsize
    max_num = -sys.maxsize
    for line in array:
        for num in line:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
    max_num = max_num - min_num
    for line_num in range(len(array)):
        for i in range(len(array[line_num])):
            array[line_num][i] = (100 * (array[line_num][i] - min_num)) / max_num
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
    return array


def main():
    array = readfile("Colorado_480x480.dat")
    print_two_d_array(array)
    array = normalize_array(array)
    print_two_d_array(array)


if __name__ == "__main__":
    main()
