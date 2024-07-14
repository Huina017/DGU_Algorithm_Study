import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

color_list = [0, 0]

def check(row_idx, col_idx, length):
    global board, color_list

    first = board[row_idx][col_idx]
    if length == 1:
        color_list[first] += 1
        return
    
    for i in range(length):
        for j in range(length):
            if board[row_idx+i][col_idx+j] != first:
                check(row_idx, col_idx, length//2)
                check(row_idx+length//2, col_idx, length//2)
                check(row_idx, col_idx+length//2, length//2)
                check(row_idx+length//2, col_idx+length//2, length//2)
                return
    color_list[first] += 1

check(0, 0, n)

print(*color_list, sep="\n")
