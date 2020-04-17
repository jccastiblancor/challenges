def word(words,dictonary,char):
    ans=True
    d = {}
    posicion = 0
    for i in words:
        if len(i)<char:
            if not d.__contains__(i[char]):
                l = []
                l.append(i)
                d[i[char]] = l
            else:
                l = d[i[char]]
                l.append(i)
                d[i[char]] = l
            for j in range(len(dictonary)):
                if dictonary[j] == i[char]:
                    if posicion > j:
                        ans = False
                        return ans
                    posicion = j

    for k in d:
        l=d[k]
        if len(l)>1:
            ans=ans and word(l,dictonary,char+1)
    return ans

words =['cab','cat','hat','tab']
dictonary=['c','h','b','t','a']
print(word(words,dictonary,0))
