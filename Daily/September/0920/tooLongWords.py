for _ in range(int(input())):
    s = input()
    if len(s) > 10:
        s = f"{s[0]}{len(s)-2}{s[-1]}"
    print(s)
