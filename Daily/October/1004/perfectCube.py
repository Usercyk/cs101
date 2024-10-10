n = int(input())

for a in range(2, n+1):
    for b in range(2, a):
        if a**3 < 3*b**3:
            break
        for c in range(b, a):
            if a**3 < b**3+2*c**3:
                break
            for d in range(c, a):
                if a**3 == b**3+c**3+d**3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                    break
