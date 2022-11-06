students = {'gryffindor': ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', ' Georges', 'Neville'],
            'ravenclaw': ['Cho', 'Luna', 'Sybill', 'Marcus', 'Marietta', 'Terry', 'Penelope'],
            'hufflepuff': ['Pomona', 'Zacharias', 'Teddy', 'Cedric', 'Nymphadora', 'Newton', 'Justin'],
            'slytherin': ['Malfoy', 'Severus', 'Dolores', 'Horace', 'Blaise', 'Pansy', 'Bellatrix']}

def winning_house(scroll):
    try:
        dico = {}
        with open(scroll, "r") as file:
            for line in file:
                if line == "":
                    break
                elem = line.split()
                student = elem[0]
                points = float(elem[1])
                for house in students:
                    if student in students[house]:
                        dico[house] = dico.get(house, 0) + points
            max = 0
            m = []
            for maison in dico:
                if dico[maison] > max:
                    max = dico[maison]
                    m = []
                if dico[maison] == max:
                    m.append(maison)
            if len(m) == 1:
                return m[0]
            else:
                return m
    except FileNotFoundError:
        raise OSError