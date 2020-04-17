def sortT(val):
    return val[2]

def twoCitySchedCost(costs):
    for i in costs:
        i.append(abs(i[0] - i[1]))

    costs.sort(key=sortT, reverse=True)
    suma = 0
    n = len(costs) / 2
    a = 0
    b = 0
    for i in costs:
        if (i[0] < i[1] and a < n) or b >= n:
            suma = suma + i[0]
            a = a + 1
        else:
            suma = suma + i[1]
            b = b + 1
    return suma
