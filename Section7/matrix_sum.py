matrix = [[39, -100, -75, 84, -7], [93, -37, 74, 76, -73]]
sum_even = 0
i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        elem = matrix[i][j]
        if elem%2 == 0:
            sum_even += matrix[i][j]
        j += 1
    i += 1