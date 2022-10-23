"""def referee(score_file):
    with open(score_file, "r") as file:
        resultats = []
        for i in file:
            resultats.append(i.strip())
        equipe_1 = [resultats[0], 0]
        equipe_2 = [resultats[1], 0]
        for j in range(2, len(resultats)):
            s = resultats[j].split(" ")
            if int(s[1]) == 150:
                return s[0]
            elif s[0] == equipe_1[0]:
                equipe_1[1] += int(s[1])
            elif s[0] == equipe_2[0]:
                equipe_2[1] += int(s[1])
        if equipe_1[1] > equipe_2[1]:
            return equipe_1[0]
        else:
            return equipe_2[0]"""


def referee(score_file):
    with open(score_file, "r") as file:
        scores = file.readlines()
        resultats1 = [scores[0].strip(), 0]
        resultats2 = [scores[1].strip(), 0]
        for i in range(2, len(scores)):
            score = scores[i].split(" ")
            if score[0] == resultats1[0]:
                resultats1[1] += int(score[1])
            elif score[0] == resultats2[0]:
                resultats2[1] += int(score[1])
            if int(score[1]) == 150:
                break
    return resultats1[0] if resultats1[1] > resultats2[1] else resultats2[0]


print(referee("C:\\Users\\marti\\LEPL1401\\Section6\\score.txt"))
