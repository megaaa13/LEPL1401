solutions = 0
a = int(input("Entrez la valeur de l'exposant a : "))
b = int(input("Entrez la valeur de l'exposant b : "))
c = int(input("Entrez la valeur de l'exposant c : "))
maximum = int(input("Entrez la valeur maximale pour x, y et z : "))
prime = True
for x in range(1, maximum):
    for y in range(1, maximum):
        for z in range(1, maximum):
            if x ** a + y ** b == z ** c:
                prime = True
                for i in range(2, max(x, y, z)):
                    if x % i == 0 and y % i == 0 and z % i == 0:
                        print(x, y, z)
                        prime = False
                        break
                if prime:
                    print("x= ", x, "y= ", y, "z= ", z)
                    solutions += 1
if solutions == 0:
    print("No solution :'(")
else:
    print("Solutions found !", solutions)
