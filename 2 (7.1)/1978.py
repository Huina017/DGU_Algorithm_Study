n = int(input())
arr = list(map(int, input().split()))

def sieve(n):
    isprime = [True]*(n+1)
    isprime[0] = isprime[1] = False
    sn = int(n**0.5)
    for i in range(2, sn+1):
        if isprime[i]:
            for j in range(i*i, n+1, i):
                isprime[j] = False
    return isprime

isprime = sieve(1000)

result = 0
for x in arr:
    if isprime[x]:
        result += 1
print(result)
