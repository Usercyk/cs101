L, N, M = map(int, input().split())
stones = [0]
for _ in range(N):
    stones.append(int(input()))
stones.append(L)

left, right = 0, L
while left < right:
    mid = (left+right)//2
    cnt, pos = 0, 0
    for i in range(1, len(stones)):
        if stones[i]-stones[pos] < mid:
            cnt += 1
        else:
            pos = i
    if cnt > M:
        right = mid
    else:
        left = mid + 1

print(left-1)
