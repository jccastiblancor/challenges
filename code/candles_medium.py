def candles2(cantidad,minimas,m):
    m.sort()
    m.reverse()
    resta = cantidad - minimas
    if minimas<cantidad*2 and resta<0:
        print('hola')
        for i in range(len(m)):
            if i==-resta:
                break
            if i % 2 == 0:
                m.append(m[i] / 2)
                m.append(m[i] / 2)
            else:
                m.append(int(m[i] / 2))
                m.append(int(m[i] / 2) + 1)
        return candles2(cantidad * 2, minimas, m)
    elif resta<0:
        n=[]
        for i in m:
            if i%2==0:
                n.append(i/2)
                n.append(i/2)
            else:
                n.append(int(i / 2))
                n.append(int(i / 2)+1)
        return candles2(cantidad*2,minimas,n)
    else:
        m.reverse()
        print(resta)
        print(m)
        return m[0]

def candles3(j,minimas,m):
    suma = 0
    for i in m:
        suma = suma+i
    opcion= int(suma/minimas)-j
    suma2=0
    for i in m:
        suma2=suma2+int(i/opcion)
    print(opcion)
    print(suma2)
    print(minimas)
    if suma2>=minimas:
        return opcion
    else:
        j=j+1
        return candles3(j,minimas,m)

data_path = "../candles2.in"
f = open(data_path, "r")
lines = f.readlines()
m=[]
for i in range(len(lines)):
  if i ==0:
    a = lines[i]
    dividir = a.split(' ')
    minimas = int(dividir[1])
  else:
    lista = lines[i]
    l = lista.split(' ')
    for i in range(len(l)):
      m.append(int(l[i]))
cantidad=0
print(candles3(cantidad,minimas,m))