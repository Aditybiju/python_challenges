
list1=list(map(int,input().split()))
c=0
for i in list1:
    if (i<0):
        c=0
        break

    else :
        n=i
        r=0
        original=i
        while(n>0):        
            d=n%10
            r=r*10+d
            n=n//10
            if original==r:
                c=1
 
if(c==0):
    print("false")
if(c==1):
    print("true")
