import itertools

n = int(input())
arr = list(map(int, input().split()))

result = list(itertools.permutations(arr, n))

max = 0
for arr in result:
    sum = 0
    for i in range(n-1):
        sum += abs(arr[i] - arr[i+1])
    if max < sum:
        max = sum
print(max)
