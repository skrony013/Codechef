T = int(input())
for t in range(T):
    def CheaperCab(a, b):
        if a < b:
            print("First")
        elif a > b:
            print("Second")
        else:
            print("Any")


    x, y = map(int, input().split())
    CheaperCab(x, y)
