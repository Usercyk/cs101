N, W = map(int, input().split())
candies = []
for _ in range(N):
    vi, wi = map(int, input().split())
    candies.append((vi, wi, vi/wi))

candies.sort(key=lambda x: x[2], reverse=True)

res = 0

for candy in candies:
    if W > candy[1]:
        res += candy[0]
        W -= candy[1]
        continue
    res += W*candy[2]
    break

print(f"{res:.1f}")
