#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    ans = 0
    graph = {}
    if c_road >= c_lib:
        ans = c_lib * n
    else:
        ## Crear grafo
        for i in range(n):
            graph[i + 1] = []
        for i in cities:
            l = graph[i[0]]
            l.append(i[1])
            graph[i[0]] = l
            l = graph[i[1]]
            l.append(i[0])
            graph[i[1]] = l

        ## Hacer DFS En todo el grafo

        visitado = [False] * (len(graph))

        for i in graph:
            if not visitado[i - 1]:
                ans = ans + c_lib
                queue = []
                queue.append(i)
                visitado[i - 1] = True

                while queue:
                    nodo = queue.pop(0)
                    l = graph[nodo]
                    for i in l:
                        if not visitado[i - 1]:
                            ans = ans + c_road
                            queue.append(i)
                            visitado[i - 1] = True
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
