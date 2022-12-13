T = int(input())
for t in range(T):
    def Outcome(a):
        listA = list(map(str,input().strip().split(' ')))
        c1 = 0
        c2 = 0
        for s in listA:
            if s == 'START38':
                c1 = c1+1
            else:
                c2 = c2+1
        print(c1, c2)
    N = int(input())
    Outcome(N)