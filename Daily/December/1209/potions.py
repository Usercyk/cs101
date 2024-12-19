from queue import PriorityQueue
n = int(input())
*a, = map(int, input().split())
hp = 0
cnt = 0
q = PriorityQueue()
for i in range(n):
    hp += a[i]
    cnt += 1
    if a[i] >= 0:
        continue
    q.put(a[i])
    if hp < 0:
        hp -= q.get()
        cnt -= 1
print(cnt)
