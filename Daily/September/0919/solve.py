# WA了……实在是不知道怎么过，难绷
from math import sqrt


for _ in range(int(input())):
    a, b, c = map(float, input().split())
    r = (-b/(2*a))
    delta = b*b-4*a*c
    if delta == 0:
        print(f"x1==x2=={'%.5f' % r}")
    elif delta > 0:
        print(
            f"x1=={'%.5f' % (r+sqrt(delta)/(2*a))};x2=={'%.5f' % (r-sqrt(delta)/(2*a))}")
    else:
        print(
            f"x1=={'%.5f' % r}+{'%.5f' % (sqrt(-delta)/(2*a))}i;x1=={'%.5f' % r}-{'%.5f' % (sqrt(-delta)/(2*a))}i")