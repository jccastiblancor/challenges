#no funciona con numeros de 2 digitos o más.
def calculadora(m):
    n=[]
    for i in m:
        if i=='+':
            n.append(i)
        elif i=='-':
            n.append(i)
        else :
            if len(n) == 0:
                suma = int(i)
            else:
                signo=n.pop()
                if signo=='+':
                    suma=suma+int(i)
                else:
                    suma=suma-int(i)
    return suma

data_path = "../data/easy_calculator.in"
f = open(data_path, "r")
lines = f.readlines()
for i in range(len(lines)):
    m=[]
    a = lines[i]
    a.replace(" ", "")
    for i in a:
        if i!='\n':
            m.append(i)
    print(calculadora(m))