import numpy as np

def espiral(n):
    ans=np.zeros((n,n))
    dir ={}
    dir[0] = [1, 0] # derecha
    dir[2] = [-1, 0]  # izquierda
    dir[3] = [0,-1]  # up
    dir[1] = [0,1]  # down
    i=n;x=0;y=0
    direccion=0
    numero=1;cambia=True

    while i>0:
        for j in range(i):
            ans[x][y]= numero
            if j==i-1:
                direccion=direccion+1
            if direccion == 4:
                direccion = 0
            x=x+dir[direccion][1]
            y=y+dir[direccion][0]
            numero=numero+1
        if cambia:
            i=i-1
            cambia=False
        else:
            cambia=True
    return ans

print(espiral(8))