for _ in range(int(input())):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:
        print(0)
    elif b <= a-x or b >= a+x:
        print(1)
    elif (a-x >= l and b >= l+x) or (a+x <= r and b <= r-x):
            print(2)
    elif (a-x<l and a+x<=r and b>=l+x) or (a+x>r and a-x>=l and b<=r-x):
        print(3)
    else:
        print(-1)