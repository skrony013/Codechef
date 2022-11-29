def ATM(n, balance):
    if n + 0.5 <= balance and n % 5 == 0:
        r = balance - (n + 0.5)
        print('%.2f' % r)
    else:
        print('%.2f' % balance)


x, y = map(float, input().split())
x = int(x)
ATM(x, y)
