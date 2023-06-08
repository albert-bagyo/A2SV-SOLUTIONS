N = int(input())
for _ in range(N):
    cnt = 0
    res = []
    n = int(input())
    if n % 2 == 0:
        print(-1)
        continue
    while n > 1:
       n = (n - 1) // 2
       if n % 2 == 0:
           res = ['1'] + res
           n = n + 1
       else:
           res = ['2'] + res
       cnt += 1
    print(cnt)
    print(" ".join(res))
