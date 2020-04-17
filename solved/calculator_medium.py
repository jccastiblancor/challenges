def calculadora(m):
    n=[]
    m.reverse()
    for i in m:
        if i=='+':
            n1=n.pop()
            n2=n.pop()
            n.append(n2+n1)
        elif i=='-':
            n1 = n.pop()
            n2 = n.pop()
            n.append(n1 - n2)
        elif i=='*':
            n1 = n.pop()
            n2 = n.pop()
            n.append(n2 * n1)
        else :
            n.append(int(i))
    return n.pop()

data_path = "../data/medium_calculator.in"
f = open(data_path, "r")
lines = f.readlines()

for i in range(len(lines)):
    m=[]
    a = lines[i]
    for i in a:
        if i!=' ' and i!='\n':
            m.append(i)
    print(calculadora(m))


#print(calculadora(m))
