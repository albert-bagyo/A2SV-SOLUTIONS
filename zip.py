N, X = map(int, input().split())
subjects = []

for _ in range(X):
    subjects.append(map(float,input().split()))

for scores in zip(*subjects):
    print(sum(scores) / X)
