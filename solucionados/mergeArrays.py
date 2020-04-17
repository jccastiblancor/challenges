def merge(A,B,C):
    a=0
    b=0
    c=0
    ans=[]
    n=len(A)+len(B)+len(C)
    for i in range(n):
        if a<len(A):
            if b<len(B):
                if c < len(C):
                    nuevo = min(A[a], B[b], C[c])
                else:
                    nuevo = min(A[a], B[b])
            else:
                if c < len(C):
                    nuevo = min(A[a], C[c])
                else:
                    nuevo = A[a]
        else:
            if b<len(B):
                if c < len(C):
                    nuevo = min(B[b], C[c])
                else:
                    nuevo = B[b]
            else:
                nuevo = C[c]
        if i==0:
            ans.append(nuevo)
        elif nuevo!=ans[len(ans)-1]:
            ans.append(nuevo)
        if a<len(A) and nuevo==A[a]:
            a=a+1
        elif b<len(B) and nuevo==B[b]:
            b=b+1
        elif c<len(C) and nuevo==C[c]:
            c=c+1
    return ans

A=[-100 ,-20,-10,0,30,40,90]
B=[-90,0,0,20,30]
C=[-50,-10,0,5,30,70,100]

print(merge(A,B,C))