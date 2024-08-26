import sys
input = sys.stdin.readline
N, C = map(int, input().split())
list1 =[]
for _ in range(N):
    i = int(input())
    list1.append(i)
list1.sort()

start, end =1, list1[-1]-list1[0]
result = 0
while start <= end:
    mid = (start+end)//2
    loc = list1[0]
    cnt =1
    for i in range(1, len(list1)):
        if(list1[i] >= loc+mid):
           cnt += 1
           loc = list1[i]
    if cnt >= C:
        start = mid +1
        result = mid
    else:
        end = mid -1
print(result)
