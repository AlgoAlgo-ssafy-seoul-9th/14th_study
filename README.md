# 14th_study

### 알고리즘 스터디 14주차

[백준 문제집](https://www.acmicpc.net/workbook/view/17523) <br/>

<!-- [프로그래머스](https://school.programmers.co.kr/learn/courses/30/lessons/148653) -->

# [흙길 보수하기]

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./흙길%20보수하기/민웅.py)

```py
# 1911_흙길보수하기_repairing-road
import sys
import heapq
input = sys.stdin.readline

N, L = map(int, input().split())

nulpange = []
endpoint = 0
cnt = 0
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(nulpange, [s, e])

while nulpange:
    S, E = heapq.heappop(nulpange)
    if E <= endpoint:
        continue

    if S > endpoint:
        for i in range(S, E, L):
            endpoint = i+L
            cnt += 1
    else:
        for i in range(endpoint, E, L):
            endpoint = i+L
            cnt += 1

print(cnt)

```

### [병국](./흙길%20보수하기/병국.py)

```py
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



```

### [상미](./흙길%20보수하기/상미.py)

```py


```

### [서희](./흙길%20보수하기/서희.py)

```py

```

### [성구](./흙길%20보수하기/성구.py)

```py


```

</div>

</details>

<br><br>

# [미네랄]

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./미네랄/민웅.py)

```py
# 2933_미네랄_minerals
import sys
from collections import deque
# input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 클러스터 내리기
def fall(cluster_lst):
    falling_length = float('inf')

    for x, y in cluster_lst:
        cnt = 0
        while True:
            if x+1 > R-1:
                break
            if cave[x+1][y] == '.':
                cnt += 1
            else:
                break

            x += 1
        if x+1 != R-1 and [x+1, y] in cluster_lst:
            continue
        if cnt < falling_length and cnt != 0:
            falling_length = cnt

    for x, y in cluster_lst:
        cave[x][y] = '.'

    for x, y in cluster_lst:
        cave[x+falling_length][y] = 'x'

# 떨어져야하는 클러스터 체크
def mineral_down(x, y):
    global cave

    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx <= R-1 and 0 <= ny <= C-1:
            if cave[nx][ny] == 'x':
                columns = [ny]
                falling_check = []
                visited = [[0]*C for _ in range(R)]
                cluster = []
                visited[nx][ny] = 1
                if nx != R-1:
                    if cave[nx+1][ny] == '.':
                        falling_check.append(ny)
                cluster.append([nx, ny])
                q = deque()
                q.append([nx, ny])

                while q:
                    lx, ly = q.popleft()

                    for di in dxy:
                        nlx = lx + di[0]
                        nly = ly + di[1]

                        if 0 <= nlx <= R-2 and 0 <= nly <= C-1:
                            if cave[nlx][nly] == 'x' and not visited[nlx][nly]:
                                q.append([nlx, nly])
                                cluster.append([nlx, nly])
                                visited[nlx][nly] = 1
                                if nly not in columns:
                                    columns.append(nly)
                                if cave[nlx+1][nly] == '.' and nly not in falling_check:
                                    falling_check.append(nly)
                falling_check.sort()
                columns.sort()
                if falling_check == columns:
                    fall(cluster)
                else:
                    continue


R, C = map(int, input().split())

cave = [list(input().strip()) for _ in range(R)]

N = int(input())
h_lst = deque(list(map(int, input().split())))
left_or_right = True


for _ in range(N):
    H = R - h_lst.popleft()
    if left_or_right:
        for i in range(C):
            if cave[H][i] == 'x':
                cave[H][i] = '.'
                mineral_down(H, i)
                break
        else:
            left_or_right = not left_or_right
            continue
    else:
        for i in range(C-1, -1, -1):
            if cave[H][i] == 'x':
                cave[H][i] = '.'
                mineral_down(H, i)
                break
        else:
            left_or_right = not left_or_right
            continue

    left_or_right = not left_or_right

for c in cave:
    print(*c, sep='')

```

## [병국](./미네랄/병국.py)

```py

```

## [상미](./미네랄/상미.py)

```py


```

## [서희](./미네랄/서희.py)

```py

```

## [성구](./미네랄/성구.py)

```py

```

</div>

</details>
