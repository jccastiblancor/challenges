def prueba():
    print('wtf esto deberia funcionar al 1000%')
def OneEditApart(s1, s2):
    resp=True
    prueba()
    if abs(len(s1)-len(s2))>1:
        return False
    l1=[]
    for c in s1:
        l1.append(c)
    i=0
    diferentes=0
    cambio=False
    for c in s2:
        if diferentes>1:
            resp=False
            break
        if len(l1)==len(s2): # Se pudo cambiar un char
            if c != l1[i]:
                diferentes=diferentes+1
        elif len(l1)>len(s2):# se quito un char.
            if cambio:
                if c != l1[i]:
                    diferentes = diferentes + 1
            else:
                if c != l1[i] and diferentes==0:
                    cambio=True
                    i=i-1
        else: # Se agrego un char
            if i>=len(l1):
                diferentes = diferentes + 1
                break
            if cambio:
                if c != l1[i]:
                    diferentes = diferentes + 1
            else:
                if c != l1[i] and diferentes==0:
                    diferentes = diferentes + 1
                    cambio=True
                    i=i-1
        i=i+1
    if diferentes==0:
        resp=False
    return resp

s1='caaat'
s2='aaaaaact'
print(OneEditApart(s1,s2))