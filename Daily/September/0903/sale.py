n, m = map(int, input().split())
b = sorted(map(lambda x: -int(x), input().split()), reverse=True)
print(sum((i for i in b[:m] if i > 0)))
