n = 10  # Fixing n, the highest number that will be calculated
sum = 0  # Initializing of the sum variable
i = 1  # Variable that will be incremented by 1 each loop
while i <= n:  # Start of the loop
    sum += i ** 2  # Sum calculation
    print(i, "\t", i ** 2, "\t", sum, "\t", (i * (i + 1) * (2 * i + 1)) // 6)  # Printing of the line
    i += 1  # Incrementation of i
