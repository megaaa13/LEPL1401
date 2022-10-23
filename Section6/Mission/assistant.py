cmds = ["exit", "file", "info", "dictionary", "search", "sum", "avg", "help"]
fiche = ""
fiche_name = ""
dico = ""
n_numbers = 0


def exit(): raise SystemExit


def file(filename):
    try:
        with open(filename, "r") as fichier:
            global fiche, fiche_name
            fiche = fichier.read()
    except FileNotFoundError:
        return "File not found !"
    else:
        fiche_name = filename
        return f"File {filename} loaded !"


def info():
    if fiche != "":
        return f"File : {fiche_name}\n" + str(len(fiche.split("\n"))) + " lines\n" + str(len(fiche)) + " caracters"
    else:
        return "Please load a file before !"


def dictionary():
    global dico
    if fiche == "":
        return "Please load a file before !"
    else:
        dico_ou_pas = fiche.split("\n")
        mot_du_dico = dico_ou_pas[0].split(",")
        try:
            int(mot_du_dico[1])
        except ValueError:
            print(dico_ou_pas[0][1])
            return f"The file {fiche_name} seems not be a dictionary..."
        else:
            dico = fiche
            return f"{fiche_name} is now used as dictionary !"


def search(word):
    if dico != "":
        for i in dico.split("\n"):
            mot = i.split(",")
            if word == mot[0]:
                return f"{word} is in the dictionary"
        else:
            return f"{word} is not in the dictionary"
    else:
        return "Please use file as a dictionary before use this"


def sum(calcul, nombre=None):
    try:
        for i in calcul.split("+"):
            float(i)
    except ValueError:
        return "\033[91mOne of the arguments is not a number !\033[0m"
    else:
        return eval(calcul)


def avg(calcul, nombre):
    try:
        for i in calcul.split("+"):
            float(i)
    except ValueError:
        if calcul == "":
            return "\033[91mPlease provide numbers to calculate the avegerage !\033[0m"
        else:
            return "\033[91mOne of the arguments is not a number !\033[0m"
    else:
        return eval(calcul) / nombre


def help():
    return """Gestionnaire de fichier : 
    file <name> : permet de charger un fichier, qui pourra ensuite être défini comme dictionnaire 
    info : permet de consulter les infos du dernier fichier chargé, comme son nombre de lignes et de caractères 
    dictionary : permet de définir le fichier chargé comme dictionnaire, afin d'effectuer des recherches à l'intérieur
    search <word> : permet de charger un mot dans le dictionnaire défini
Calculatrice :
    sum <number1> <number2> ... <number n> : permet de calculer la somme de nombres entrés
    avg <number1> <number2> ... <number n> : permet de calculer la moyenne de nombres entrés
Miscellaneous :
    help : affiche ceci
    exit : permet d'arrêter l'assistant"""


def main():
    while True:
        cmd = input("\033[96m> \033[0m")
        f = cmd.split()
        command = f[0]
        f.remove(command)
        args = ", ".join(f)
        if command in cmds:
            try:
                if command in ["sum", "avg"]:
                    global n_numbers
                    n_numbers = len(f)
                    calculus = "+".join(f)
                    print(eval(command + "(calculus, n_numbers)"))
                elif args != "":
                    print(eval(command + "(args)"))
                elif args == "":
                    print(eval(command + "()"))
            except TypeError as err:
                print(f"Missing arguments in the command !\n\033[91m{err}\033[0m")
            except NameError as err:
                print(f"Error during calculation !\n\033[91m{err}\033[0m")


if __name__ == '__main__':
    main()
