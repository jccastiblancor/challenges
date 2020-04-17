def candles(cantidad,minimas,m):
  ans=0
  resta=cantidad-minimas
  m.sort()
  print(resta)
  return m[resta]

data_path = "../candles.in"
f = open(data_path, "r")
lines = f.readlines()
m=[]
for i in range(len(lines)):
  if i ==0:
    a = lines[i]
    dividir = a.split(' ')
    cantidad = int(dividir[0])
    minimas = int(dividir[1])
  else:
    lista = lines[i]
    l = lista.split(' ')
    for i in range(len(l)):
      m.append(int(l[i]))


print(len(m))
print(candles(cantidad,minimas,m))