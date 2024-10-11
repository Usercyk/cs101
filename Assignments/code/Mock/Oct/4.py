n = int(input())
while True:
    if n == 1:
        print("End")
        break
    if n % 2 == 0:
        print(f"{n}/2={n//2}")
        n //= 2
    else:
        print(f"{n}*3+1={n*3+1}")
        n = n*3+1
