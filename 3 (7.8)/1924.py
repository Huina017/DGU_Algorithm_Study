import sys

def solve():
    x, y = map(int, sys.stdin.readline().rstrip().split())
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diff = sum(day[0:x]) + y - 1
    r = diff % 7
    if r == 0:
        print("MON")
    elif r == 1:
        print("TUE")
    elif r == 2:
        print("WED")
    elif r == 3:
        print("THU")
    elif r == 4:
        print("FRI")
    elif r == 5:
        print("SAT")
    elif r == 6:
        print("SUN")
        
solve()
