t = int(input())
for i in range(t):
    N = int(input())
    S = input()
    c = 0
    filp_bits = ''
    if S.count('1') > S.count('0'):
        for j in S:
            if j == '0':
                filp_bits += '1'
            else:
                filp_bits += '0'
        print(filp_bits.count('1') +1)
    else:
        print(S.count('1'))
