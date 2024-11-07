import re


for _ in range(int(input())):
    place = input()
    l = re.findall(r"R(\d+)C(\d+)", place)
    if l:
        x, y = map(int, l[0])
        col = ""
        while y:
            r = y % 26
            s = chr(ord("A")+r-1) if r > 0 else "Z"
            col = s+col
            y //= 26
            if r == 0:
                y -= 1
        print(col+str(x))
    else:
        l = re.findall(r"([A-Z]+)(\d+)", place)
        y, x = l[0]
        col = 0
        while y:
            r = y[0]
            s = ord(r)-ord("A")+1
            col = col*26+s
            y = y[1:]
        print(f"R{x}C{col}")
