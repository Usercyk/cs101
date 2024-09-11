input()
ls = list(map(lambda x: int(x) % 2, input().split(" ")))
a = ls[0]
b = ls[1]
if a == b:
    for i, v in enumerate(ls):
        if v != a:
            print(i+1)
elif a == ls[2]:
    print(2)
else:
    print(1)
