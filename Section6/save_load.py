import json


def save_data(filename, life, mana, position_x, position_y):
    with open(filename, "w") as file:
        x = {
            "life": life,
            "mana": mana,
            "x": position_x,
            "y": position_y
        }
        file.write(json.dumps(x))


def load_data(filename):
    try:
        with open(filename, "r") as file:
            x = json.loads(file.read())
            return x["life"], x["mana"], x["x"], x["y"]
    except FileNotFoundError as err:
        with open(filename, "w") as file:
            x = {
                "life": 100,
                "mana": 100,
                "x": 0,
                "y": 0
            }
            file.write(json.dumps(x))
            print("Pas de sauvegarde trouvée, création d'un nouveau fichier")


#Without JSON
def save_data(filename, life, mana, position_x, position_y):
    with open(filename, "w") as file:
        file.write(f"{life} {mana} {position_x} {position_y}")

def load_data(filename):
    try:
        with open(filename, "r") as file:
            lst = file.readline().split(" ")
            for n,i in enumerate(lst):
                lst[n] = int(i)
                tup = tuple(lst)
        return tup
    except:
        raise FileNotFoundError
save_data("data.json", 1, 1, 1, 1)
print(load_data("data.json"))
