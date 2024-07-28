import sys
import heapq as hq

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
  x = int(sys.stdin.readline().strip())  
  if x:
    hq.heappush(heap, (-x))
  else:
    try:
      print(-1 * hq.heappop(heap))
    except:
      print(0)
