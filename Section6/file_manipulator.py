def line_count(filename):
    with open(filename, "r") as file:
        return len(file.readlines())


def char_count(filename):
    with open(filename, "r") as file:
        return len(file.read())


def space(filename, n):
    with open(filename, "w") as file:
        file.write(" " * n)


def capitalize(filename_in,filename_out):
    with open(filename_in, "r") as file1:
        data = file1.read().upper()
    with open(filename_out, "w") as file2:
        file2.write(data)


print(line_count("streets.txt"))
print(char_count("streets.txt"))
space("lavi.txt", 10)
capitalize("streets.txt", "CAPSSTREETS.TXT")