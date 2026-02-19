from collections import deque
def solve():
    caps = (8, 5, 3)
    target = 4
    initial = (8, 0, 0)
    q = deque([(initial, [initial])])
    visited = {initial}
    while q:
        curr, path = q.popleft()
        if any(x ==