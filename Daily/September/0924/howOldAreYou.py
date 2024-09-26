s = int(input())
while s != 1:
    if s % 2 == 1:
        print(f"{s}*3+1={s*3+1}")
        s = s*3+1
    else:
        print(f"{s}/2={s//2}")
        s //= 2
