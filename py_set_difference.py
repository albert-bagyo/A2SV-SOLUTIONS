# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
total = sys.stdin.readline()
english = set( [int(a) for a  in sys.stdin.readline().split(" ")])
total_french = sys.stdin.readline()
french = set( [int(a) for a  in sys.stdin.readline().split(" ")])
    
print(len(english.difference(french)))
