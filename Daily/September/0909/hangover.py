while True:
    n = input()
    if n == "0.00":
        break
    n = float(n)
    sum = 0
    for i in range(2, 281):
        sum += 1/i
        if sum >= n:
            print(f"{i-1} card(s)")
            break
