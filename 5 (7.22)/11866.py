import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
answer = []

queue = deque()
for i in range(n):
    queue.append(i+1)

while queue:
    queue.rotate(-k)
    m = queue.pop()
    answer.append(m)

print("<" + str(answer)[1:-1] + ">")
