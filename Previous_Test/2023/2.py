n, a, b = map(int, input().split())
*plants, = map(int, input().split())
cnt = 0
i, j = 0, n-1
pot_a, pot_b = a, b
while i < j:
    if pot_a < plants[i]:
        cnt += 1
        pot_a = a
    if pot_b < plants[j]:
        cnt += 1
        pot_b = b
    pot_a -= plants[i]
    pot_b -= plants[j]
    i += 1
    j -= 1
if i == j and max(pot_a, pot_b) < plants[i]:
    cnt += 1


print(cnt)
