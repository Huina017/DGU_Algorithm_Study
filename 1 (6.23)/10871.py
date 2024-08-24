n, x = map(int,input().split())
a = list(map(int,input().split()))

print(' '.join(map(str,[i for i in a if i<x])))
