# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n = int(input())

occ = defaultdict(int)

for _ in range(n):
    occ[input()] += 1
    
print(len(occ))
print(" ".join([str(v) for k,v in occ.items()]))
