borrowed_money = {}


def give_money(borrowed, from_person, to_person, amount):
    if type(from_person) != str or type(to_person) != str or type(borrowed) != dict:
        raise ValueError("ALED")
    if type(amount) != float:
        if type(amount) != int:
            raise ValueError("JPP")
    if from_person not in borrowed:
        borrowed[from_person] = {}
    if to_person not in borrowed:
        borrowed[to_person] = {}
    if from_person not in borrowed[to_person]:
        borrowed[to_person][from_person] = 0
    if to_person not in borrowed[from_person]:
        borrowed[from_person][to_person] = 0
    borrowed[from_person][to_person] -= amount
    borrowed[to_person][from_person] += amount


def total_money_borrowed(borrowed):
    if type(borrowed) != dict:
        raise ValueError
    total = 0
    for cash in borrowed.values():
        for i in cash.values():
            if i > 0:
                total += i
    return total


give_money(borrowed_money, "Mark", "Bill", 2000000)
give_money(borrowed_money, "Mark", "Steve", 2000000)
give_money(borrowed_money, "Serguei", "Bill", 5000000)
give_money(borrowed_money, "Bill", "Larry", 6000000)
give_money(borrowed_money, "Larry", "Linus", 5.5)
give_money(borrowed_money, "Steve", "Mark", 2000000)
