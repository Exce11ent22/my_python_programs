def amount_triangles(N):
    amount = 0
    for i in range(1, N + 1):
        for k in range(1, i + 1):
            if k*2 <= i and i%2 == 0:
                amount += (i - (k-1)) + (1 + 2*(int(i/2) - k))
            elif k*2 < i and i%2 != 0:
                amount += (i - (k-1)) + (2 + 2*(int(i/2) - k))
            else:
                amount += i - k + 1
    return amount

while True:
    print(amount_triangles(int(input())))
