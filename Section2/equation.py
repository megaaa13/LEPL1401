solutions = 0
a = int(input("Entrez la valeur de l'exposant a : "))
b = int(input("Entrez la valeur de l'exposant b : "))
c = int(input("Entrez la valeur de l'exposant c : "))
maximum = int(input("Entrez la valeur maximale pour x, y et z : "))
for x in range(1, maximum):
    for y in range(1, maximum):
        for z in range(1, maximum):
            if x ** a + y ** b == z ** c:
                print("x= ", x, "y= ", y, "z= ", z)
                solutions += 1
if solutions == 0:
    print("No solution (╯°□°）╯︵ ┻━┻")
else:
    print("Solutions found !", solutions)
