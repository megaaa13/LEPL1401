knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
             ['Ravenclaw', ['smart', 'wise', 'curious']],
             ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
             ['Slytherin', ['cunning', 'wily', 'malignant']]]


def house_designation(student_qualities):
    result = []
    choice = [0, 0, 0, 0]
    finals = []
    g, r, h, s = 0, 0, 0, 0
    for house in knowledge:
        for qualities in student_qualities:
            if qualities in house[1]:
                result.append(house[0])
    for houses in result:
        if houses == "Gryffindor":
            choice[0] += 1
            g += 1
        elif houses == 'Ravenclaw':
            choice[1] += 1
            r += 1
        elif houses == 'Hufflepuff':
            choice[2] += 1
            h += 1
        elif houses == 'Slytherin':
            choice[3] += 1
            s += 1
    choice.sort(reverse=True)
    print(g, r, s, h)
    for n in choice:
        if n == g:
            finals.append("Gryffindor")
            g = None
        elif n == r:
            finals.append('Ravenclaw')
            r = None
        elif n == h:
            finals.append('Hufflepuff')
            h = None
        elif n == s:
            finals.append('Slytherin')
            s = None
    return finals

print(house_designation(["brave", "strong", "smart", "wise", "loyal"]))
