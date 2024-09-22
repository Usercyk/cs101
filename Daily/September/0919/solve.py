from math import sqrt


for _ in range(int(input())):
    a, b, c = map(float, input().split())
    if b == -0.0:
        b = -b
    r = -b/(2*a)
    delta = b*b-4*a*c
    if delta == 0:
        print(f"x1=x2={r:.5f}")
    elif delta > 0:
        print(
            f"x1={(r+sqrt(delta)/(2*a)):.5f};x2={(r-sqrt(delta)/(2*a)):.5f}")
    else:
        print(
            f"x1={r:.5f}+{(sqrt(-delta)/(2*a)):.5f}i;x2={r:.5f}-{(sqrt(-delta)/(2*a)):.5f}i")
