i = ...    # le nombre à tester (i >= 1)
temp = ... # "fizz", "buzz", "fizzbuzz" ou "no" en fonction de la valeur de i

if i % 3 == 0 and i % 5 == 0:
    temp = "fizzbuzz"
elif i % 3 == 0:
    temp = "fizz"
elif i % 5 == 0:
    temp = "buzz"
else :
    temp = "no"