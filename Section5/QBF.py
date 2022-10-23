import math

trace1 = [(1.0, (10.10, 20.0)), (3.0, (10.50, 20.30)), (5.0, (11.0, 21))]
trace2 = [(1.0, (15.00, 15.0)), (2.0, (12.00, 17.00)), (3.0, (10.50, 20)), (4.0, (12.0, 21.0))]
trace3 = [(1.0, (15.00, 15.0)), (3.0, (16.0, 21.0)), (5.0, (20.0, 21.0))]
l = [trace1, trace2, trace3]


def absolute(v1, v2):
    return abs(v1 - v2)


def euclidian_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)


def matrix_for_traces(l, theta_1, theta_2):
    matrix = []
    for i in range(len(l)):
        submatrix = []
        for j in range(len(l)):
            submatrix.append(0)
        matrix.append(submatrix.copy())
    for n, trace_1 in enumerate(l):
        for m, trace_2 in enumerate(l):
            for elem in trace_1:
                for elem1 in trace_2:
                    if absolute(elem[0], elem1[0]) <= theta_1 and euclidian_distance(elem[1], elem1[1]) < theta_2:
                        matrix[n][m] = 1
                        break
    return matrix


print(matrix_for_traces(l, 0.0, 1.0))
print(matrix_for_traces([[(1.0, (10.1, 20.0)), (3.0, (10.5, 20.3)), (5.0, (11.0, 21))],
                         [(1.0, (15.0, 15.0)), (2.0, (12.0, 17.0)), (3.0, (10.5, 20)), (4.0, (12.0, 21.0))]], 0.0, 0.0))