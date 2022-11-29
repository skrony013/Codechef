import math

T = int(input())
for t in range(T):

    def isPrime(n):
        count = 0
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                print("Bob")
                break
            count += 1
        if count + 2 == math.floor(math.sqrt(n))+1:
            print("Alice")


    x, y = map(int, input().split())
    r = x + y
    isPrime(r)

