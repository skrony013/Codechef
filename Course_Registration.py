T = int(input())
for t in range(T):
    def CourseReg(a, b, c):
        if b - c >= a:
            print("Yes")
        else:
            print("No")


    N, M, K = map(int, input().split())
    CourseReg(N, M, K)
