input()
last = 0
for s in map(int, input().split()):
    if s >= last:
        last = s
    else:
        print("NO")
        break
else:
    print("YES")
