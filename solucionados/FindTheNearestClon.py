#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    grafo = {}
    for i in range(graph_nodes):
        grafo[i + 1] = []
    for i in range(len(graph_from)):
        l = grafo[graph_from[i]]
        l.append(graph_to[i])
        grafo[graph_from[i]] = l
        l = grafo[graph_to[i]]
        l.append(graph_from[i])
        grafo[graph_to[i]] = l

    visitado = [False] * graph_nodes
    distancia = 0
    queue = []
    encontro = False
    for i in range(graph_nodes):
        if ids[i] == val:
            queue.append(i + 1)
            visitado[i] = True
            break
    cont = 1
    ck = 0
    while queue:
        nodo = queue.pop(0)
        ck = ck + 1
        l = grafo[nodo]
        if ck == cont:
            ck = 0
            distancia = distancia + 1
            cont = len(l)
        for i in l:
            if not visitado[i - 1]:
                if ids[i - 1] == val:
                    encontro = True
                    break
                queue.append(i)
                visitado[i - 1] = True
    if not encontro:
        distancia = -1
    return distancia


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
