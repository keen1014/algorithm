import sys
input=sys.stdin.readline
R, C, M=map(int, input().strip().split())
board=[[None] * (C) for _ in range(R)]

for i in range(M):
    r, c, s, d, z=map(int, input().strip().split())
    board[r-1][c-1]=(s, d, z)
def get_next_loc(n, cur, speed, direction):
    cycle = (n - 1) * 2

    if direction == 1 or direction ==4:
        temp = cycle - cur
    else:
        temp = cur
    temp = (temp + speed) % cycle

    if temp < n:
        next_pos = temp
        next_dir = 2 if direction <=2 else 3
        if next_pos == n -1:
            next_dir = 1 if direction <= 2 else 4
    else:
        next_pos = cycle -temp
        next_dir = 1 if direction <= 2 else 4
        if next_pos == 0:
            next_dir = 2 if direction <= 2 else 3
    return next_pos, next_dir

answer=0
for fisher in range(C):
    for r in range(R):
        if board[r][fisher]:
            answer += board[r][fisher][2]
            board[r][fisher] = None
            break
    new_board = [[None] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c]:
                s, d, z = board[r][c]

                if d ==1 or d == 2:
                    nr, nd = get_next_loc(R, r, s, d)
                    nc = c
                else:
                    nc, nd = get_next_loc(C, c, s, d)
                    nr = r

                if new_board[nr][nc]:
                    if new_board[nr][nc][2] < z:
                        new_board[nr][nc] = (s, nd, z)

                else:
                    new_board[nr][nc] = (s, nd, z)
    board = new_board

print(answer)