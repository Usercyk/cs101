n = 1
while True:
    p, e, i, d = map(int, input().split())
    if p == e == i == d == -1:
        break
    # x=p+23x=e+28y=i+33z
    # (23*28)^(-1) = 2  mod 33
    # (28*33)^(-1) = 6  mod 23
    # (23*33)^(-1) = 19 mod 28
    x = (p*28*33*6+e*23*33*19+i*23*28*2) % 21252
    x = x if x else 21252
    s = x-d if x-d > 0 else x-d+21252
    print(f"Case {n}: the next triple peak occurs in {s} days.")
    n += 1
