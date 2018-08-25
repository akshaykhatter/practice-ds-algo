# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def setAtLocation(matrix, coords, value):
    matrix[coords[0]][coords[1]] = value

def getFromLocation(matrix, coords):
    return matrix[coords[0]][coords[1]]

def matrixRotation(matrix):
    count = min(m, n) // 2 # no of loops/layers
    layers = []

    for l_index in range(count):
        i_upper = j_left = 0 + l_index
        i_lower = (m - 1) - l_index
        j_right = (n - 1) - l_index
        layer = []

        # left vertical
        for i in range(i_upper, i_lower + 1):
            layer.append((i, j_left))

        # lower horizontal
        for j in range(j_left + 1, j_right + 1):
            layer.append((i_lower, j))

        # right vertical
        for i in range(i_lower - 1, i_upper - 1, -1):
            layer.append((i, j_right))

        # upper horizontal
        for j in range(j_right - 1, j_left, -1):
            layer.append((i_upper, j))

        layers.append(layer)

    for layer in layers:
        front_array = []

        if r > len(layer):
            r_effective = r % len(layer)
        else:
            r_effective = r

        for i in range(len(layer) - r_effective, len(layer)):
            front_array.append(getFromLocation(matrix, layer[i]))
        
        for i in range(len(layer) - 1, r_effective - 1, -1):
            value = getFromLocation(matrix, layer[i - r_effective])
            setAtLocation(matrix, layer[i], value)
        
        for i in range(len(front_array)):
            setAtLocation(matrix, layer[i], front_array[i])
            

    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print("")

if __name__ == '__main__':
    mnr = input().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    print("")

    matrixRotation(matrix)