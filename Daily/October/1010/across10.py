s = input()
maxv = 1
cur = 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        cur += 1
        continue
    maxv = max(maxv, cur)
    cur = 1
maxv = max(maxv, cur)
print(maxv)
