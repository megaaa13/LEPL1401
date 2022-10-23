def get_max(filename):
    try:
        with open(filename, "r") as file:
            maximum = 0
            for i in file.readlines():
                ok = True
                try:
                    float(i.strip())
                    if float(i.strip()) < 0:
                        raise ValueError("ALED")
                except ValueError:
                    ok = False
                else:
                    if float(i.strip()) > maximum:
                        y = float(i.strip())
                        if y == int(y):
                            maximum = int(y)
                        else:
                            maximum = float(i)
            if not ok and maximum == 0:
                return -1
            else:
                return maximum
    except:
        return -1


print(get_max("numbers.txt"))
