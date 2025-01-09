from collections import deque
while True:
    s, e = map(int, input().split())
    if s == e == 0:
        break
    vis = set()
    vis.add(s)
    q = deque()
    q.append((0, s, ""))

    while q:
        step, pos, path = q.popleft()
        if pos == e:
            print(step)
            print(path)
            break
        if pos*3 not in vis:
            vis.add(pos*3)
            q.append((step+1, pos*3, path+"H"))
        if pos//2 not in vis:
            vis.add(pos//2)
            q.append((step+1, pos//2, path+"O"))
