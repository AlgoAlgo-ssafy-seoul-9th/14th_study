n,l = map(int,input().split())
# n 물웅덩이개수, l 널빤지 길이
board = [list(map(int,input().split())) for _ in range(n)]
board.sort()
maxx = board[-1][-1]
cnt = 0
now = board[0][0]
for i in range(len(board)):
    start,end = board[i][0], board[i][1]
    if start > now:
        now = start
    while True:
        if now>=end:
            break
        else:
            now += l
            cnt += 1
print(cnt)

