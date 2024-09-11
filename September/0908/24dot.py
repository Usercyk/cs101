m = int(input())
for _ in range(m):
    a, b, c, d = map(int, input().split(" "))
    if any((a+b+c+d == 24, a+b+c-d == 24, a+b-c+d == 24, a+b-c-d == 24, a-b+c+d == 24, a-b+c-d == 24, a-b-c+d == 24, a-b-c-d == 24, -a+b+c+d == 24, -a+b+c-d == 24, -a+b-c+d == 24, -a+b-c-d == 24, -a-b+c+d == 24, -a-b+c-d == 24, -a-b-c+d == 24)):
        print("YES")
    else:
        print("NO")
