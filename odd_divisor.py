t = int(input())
for _ in range(t):
    n = int(input())
    res = 'NO'
    while n > 1:
        if n % 2 == 1:
            res = 'YES'
            break
        else:
            n = n // 2
    
    print(res)
