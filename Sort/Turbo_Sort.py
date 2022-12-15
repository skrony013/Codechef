listA = []
t = int(input())
while t>0:
    n = int(input())
    listA.append(n)
    t -=1
listA.sort()
for i in listA:
    print(i)

