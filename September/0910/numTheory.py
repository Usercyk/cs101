def factor(n):
    ls = []
    while (n > 1):
        for i in range(2, n+1):
            if n % i == 0:
                ls.append(i)
                n //= i
                break
    return ls


n = int(input())
ls = factor(n)
s = set(ls)
if len(s) != len(ls):
    print(0)
elif len(s) % 2 == 0:
    print(1)
else:
    print(-1)
