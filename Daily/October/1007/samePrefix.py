s = []
for _ in range(int(input())):
    s.append(input())
res = ""
for k in map(set, zip(*s)):
    if len(k) != 1:
        break
    res += k.pop()
print(res)
