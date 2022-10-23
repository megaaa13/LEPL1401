def write_coordinates(filename, l):
    with open(filename, "w") as file:
        for i in range(len(l)):
            if i != len(l) - 1:
                file.write(str(l[i][0]) + "," + str(l[i][1]) + "\n")
            else:
                file.write(str(l[i][0]) + "," + str(l[i][1]))


def read_coordinates(filename):
    with open(filename, "r") as file:
        c = []
        for i in file.readlines():
            data = i.split(",")
            c.append((float(data[0]), float(data[1].strip())))
    return c


write_coordinates("cos.txt", [(0.5, 0.5), (0.1, 0.3), (0.4, 0.5)])
print(read_coordinates("cos.txt"))
