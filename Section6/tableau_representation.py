def table(filename_in, filename_out, width):
    with open(filename_in, "r") as file:
        lignes = []
        for line in file:
            lignes.append(line.rstrip())

    with(open(filename_out, "w")) as file:
        file.write("+{}+\n".format("-" * (width + 2)))
        for ligne in lignes:
            file.write("| {}{} |\n".format(ligne[:width], " " * (width - len(ligne))))
        file.write("+{}+".format("-" * (width + 2)))


table("villes.txt", "villestab.txt", 2)
