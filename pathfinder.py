def print_two_d_array(item):
    for num in range(len(item)):
        print(item[num])


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
    array = readfile("testMountains.dat")
    print_two_d_array(array)


if __name__ == "__main__":
    main()
