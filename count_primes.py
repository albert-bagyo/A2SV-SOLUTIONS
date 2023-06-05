class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        if n == 2:
            return 0
        primes = [True] * (n)
        primes[0] = False
        primes[1] = False
        count = 0

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i**2, n, i):
                    primes[j] = False

        for i in range(n):
            if primes[i]:
                count += 1

        return count
