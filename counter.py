from collections import Counter
money = 0
X = int(input())
shoes = [a for a in  map(int, input().split())]
N = int(input())
count  = Counter(shoes)
for i in range(N):
    size, price = map(int, input().split())
    if count[size] != 0:
        money += price
        count[size] -= 1
        
        
print(money)
