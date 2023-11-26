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

## [민웅](<./미네랄/민웅.py>)

```py

```

## [병국](<./미네랄/병국.py>)

```py

```

## [상미](<./미네랄/상미.py>)

```py


```

## [서희](<./미네랄/서희.py>)

```py

```

## [성구](<./미네랄/성구.py>)

```py

```

</div>

</details>