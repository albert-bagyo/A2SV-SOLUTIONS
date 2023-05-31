# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

A = set([int(a) for a in sys.stdin.readline().split(" ")])
n = int(sys.stdin.readline())
result = "True"
for i in range(n):
    B = set([int(a) for a in sys.stdin.readline().split(" ")])
    if not A.issuperset(B) or A == B:
        result = "False"
        break
    
print(result)
