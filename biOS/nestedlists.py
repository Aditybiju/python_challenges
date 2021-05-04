number_students=int(input())
mark=[]
name=[]
listofscores=[]

for i in range (number_students):

    name=input()
    score=float(input())
    listofscores.append([name,score])
    mark.append(score)
mark=sorted(mark)
#print(listofscores)
#print(mark)

m=mark[1]
name=[]
for j in listofscores:
    if m==j[1]:
        name.append(j[0])
name.sort()
for k in name:
    print(k)
