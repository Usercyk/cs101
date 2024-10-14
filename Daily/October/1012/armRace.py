p = int(input())
s = sorted(map(int, input().split()))
arm = 0
oarm = 0
i = 0
j = len(s)-1

while i <= j:
    if p >= s[i]:
        p -= s[i]
        arm += 1
        i += 1
        continue
    if arm > oarm and i < j:
        p += s[j]
        oarm += 1
        j -= 1
        continue
    break

print(arm-oarm)
