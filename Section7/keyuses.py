def get_country(lst, name):
    for i in lst:
        if i["City"] == name:
            return i["Country"]
    else:
        return False