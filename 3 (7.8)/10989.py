import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10001

for i in range(n):
    input_num = int(input())
    arr[input_num] = arr[input_num] + 1
    
for i in range(10001):
    if arr[i]:
        for j in range(arr[i]):
            print(i)
