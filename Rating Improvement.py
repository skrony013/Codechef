T = int(input())
for t in range(T):
    def RatingImprovement(a, b):
        if a <= b <= a + 200:
            print("YES")
        else:
            print("NO")


    x, y = map(int, input().split())
    RatingImprovement(x, y)
