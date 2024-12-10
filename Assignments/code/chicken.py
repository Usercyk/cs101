n, k = map(int, input().split())
t = sorted(map(int, input().split()))
sum_t = sum(t)

while t[-1] > sum_t/k:
    sum_t -= t.pop()
    k -= 1

print(f"{sum_t/k:.3f}")
