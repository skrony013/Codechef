T = int(input())
for t in range(T):
    def burger(p, b):
        if p < b:
            print(p)
        else:
            print(b)


    A, B = map(int, input().split())

    burger(A, B)
