def operacion(op,numbers,data):
    if len(numbers) > 1:
        if type(numbers[len(numbers)-2]) == int and type(numbers[len(numbers)-1]) == int:
            n1 = numbers.pop()
            n2 = numbers.pop()
            if op=='-':
                numbers.append(n1 - n2)
            elif op=='+':
                numbers.append(n1 + n2)
            elif op=='*':
                numbers.append(n1 * n2)
        else:
            numbers.append(data)
    else:
        numbers.append(data)

def calculadora(ans,m):
    n=[]
    m.reverse()
    pasoX=False
    for i in range(len(m)):
        if m[i]=='X':
            numbers=[]
            pasoX=True
        elif m[i]=='+':
            if pasoX:
                operacion('+',numbers,m[i])
            else:
                n1=n.pop()
                n2=n.pop()
                n.append(n2+n1)
        elif m[i]=='-':
            if pasoX:
                operacion('-',numbers,m[i])
            else:
                n1=n.pop()
                n2=n.pop()
                n.append(n1 - n2)
        elif m[i]=='*':
            if pasoX:
                operacion('*', numbers,m[i])
            else:
                n1=n.pop()
                n2=n.pop()
                n.append(n2*n1)
        else :
            if pasoX:
                numbers.append(int(m[i]))
            else:
                n.append(int(m[i]))

    numbers.reverse()
    n.reverse()
    anterior=numbers[0]
    if anterior=='-':
        anterior='+'
    for i in range(len(numbers)-1):
        actual=numbers[i+1]
        if type(anterior)==str and type(actual)==int:
            if anterior == '*':
                ans = ans / actual
            elif anterior == '+':
                ans = ans - actual
            elif anterior == '-':
                ans = ans + actual
        elif type(anterior)==str and type(actual)==str:
            ultimo=n.pop()
            if anterior == '*':
                ans = ans / ultimo
            elif anterior == '+':
                ans = ans - ultimo
            elif anterior == '-':
                ans = ans + ultimo
        anterior=actual

    for i in range(len(n)):
        actual = n[i]
        if type(anterior)==str and type(actual)==int:
            if anterior=='*':
                ans=ans/actual
            elif anterior=='+':
                ans=ans-actual
            elif anterior=='-':
                ans=ans+actual
        anterior=actual
    return ans

data_path = "../data/hard_calculator.in"
f = open(data_path, "r")
lines = f.readlines()

for i in range(len(lines)):
    m=[]
    a = lines[i]
    a.strip("\n")
    div=a.split(' ')
    ans=int(div[0])
    a=div[1:]
    a[len(a)-1].strip("\n")
    for i in a[len(a)-1]:
        if i!=' ' and i!='\n':
            a[len(a)-1]=i
    print(calculadora(ans,a))