a,c,o,e=[],[],[],[]
n=sorted(input())
for i in n:
    if i.isalpha():
        if i.isupper():
            x = c
        else:
            x=a
    else:
        if int(i)%2:
         x = o 
        else:
         x= e
    x.append(i)
print("".join(a+c+o+e))