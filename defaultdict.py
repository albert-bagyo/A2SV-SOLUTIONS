n, m = [int(a) for a in input().split()]
for _ in range(n):
    A.append(input())

for i in range(m):
    word = input()
    B.append(word)
    for j in range(n):
        if word == A[j]:
            occurances[word].append(str(j + 1))
            
for k in B:
    if occurances[k]:
        print(" ".join(occurances[k]))
    else:
        print(-1)
