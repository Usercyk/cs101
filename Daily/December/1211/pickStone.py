def check(a, b):
    a, b = max(a, b), min(a, b)
    return b == 0 or a == b or a/b >= 2 or not check(b, a-b)


while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print("win" if check(a, b) else "lose")
