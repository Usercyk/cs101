input()
coins = sorted(map(int, input().split()),reverse=True)
curr = 0
left = sum(coins)
for i, c in enumerate(coins):
    curr += c
    left -= c
    if curr > left:
        print(i+1)
        break
