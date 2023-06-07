class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        first = 0
        second = 0
        p = 1
        for i in range(-1,-len(num1)-1,-1):
                first += m[num1[i]] * p
                p *= 10
        p = 1
        for i in range(-1,-len(num2)-1,-1):
                second += m[num2[i]] * p
                p *= 10
    
        return str(first * second)
