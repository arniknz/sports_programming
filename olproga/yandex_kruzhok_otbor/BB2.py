"""from collections import deque
import heapq

ochered = deque()
pr_ochered = []
f = False

for _ in range(int(input())):
    s = input().split()
    if len(s) == 2:
        if f:
            heapq.heappush(pr_ochered, -int(s[1]))
        else:
            ochered.appendleft(int(s[1]))
    else:
        if s[0] == 'level':
            f = True
            while ochered:
                heapq.heappush(pr_ochered, -ochered.pop())
        else:
            if f:
                print(-heapq.heappop(pr_ochered))
            else:
                print(ochered.pop())"""


from collections import deque
import heapq

ochered = deque()
st_ochered = []

for _ in range(int(input())):
    s = input().split()
    if len(s) == 2:
        ochered.appendleft(int(s[1]))
    else:
        if s[0] == 'level':
            while ochered:
                heapq.heappush(st_ochered, ochered.popleft())
        else:
            if st_ochered:
                print(heapq.heappop(st_ochered))
            else:
                print(ochered.pop())