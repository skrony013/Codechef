n1 = int(input())
n2 = int(input())

m = n1 * n2

while n2 != 0:
    rem = n1 % n2
    n1 = n2
    n2 = rem
print('GCD', n1)
print("LCM", m // n1)
