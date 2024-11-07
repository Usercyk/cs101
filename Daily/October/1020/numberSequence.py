"""
1                   1                           1
1...k               k                           k(k+1)/2
123456789           9                           45

12345678910         11                          56
1...10...k          9+(k-9)*2=2k-9              k^2-8k+36
1...99              189                         9045

1...99100           192                         9237
1...100...k         189+(k-99)*3=3k-108         3k^2/2-213k/2+4887
1...999             2889                        1395495

1...9991000         2893                        1398388
1...1000...k        2889+(k-999)*4=4k-1107      2k^2-1105k+503388
1...9999            38889                       189414495

1...999910000       38894                       189453389
1...10000...k       38889+(k-9999)*5=5k-11106   5k^2/2-22207k/2+50488389
1...10000...31268                               2147523711
"""


def find(idx):
    if idx <= 9:
        return idx
    if idx <= 189:
        p = (idx+9)//2
        if idx % 2 == 1:
            return p % 10
        else:
            return (p+1)//10
    if idx <= 2889:
        p = (idx+108)//3
        if idx % 3 == 0:
            return p % 10
        elif idx % 3 == 1:
            return (p+1) // 100
        else:
            return (p+1)//10 % 10
    if idx <= 38889:
        p = (idx+1107)//4
        if idx % 4 == 1:
            return p % 10
        elif idx % 4 == 2:
            return (p+1)//1000
        elif idx % 4 == 3:
            return (p+1) % 100//100
        else:
            return (p+1)//10 % 10
    p = (idx+11106)//5
    if idx % 5 == 4:
        return p % 10
    elif idx % 5 == 0:
        return (p+1)//10000
    elif idx % 5 == 1:
        return (p+1) % 10000//1000
    elif idx % 5 == 2:
        return (p+1) % 1000//100
    else:
        return (p+1)//10 % 10


def solve(n):
    if n <= 45:
        for k in range(1, 10):
            if k*(k+1)//2 >= n:
                return find(n-k*(k-1)//2)
    if n <= 9045:
        for k in range(10, 100):
            if k*k-8*k+36 >= n:
                return find(n-k*k+10*k-45)
    if n <= 1395495:
        for k in range(100, 1000):
            if (3*k*k-213*k)//2+4887 >= n:
                return find(n-3*(k-72)*(k-1)//2-4887)
    if n <= 189414495:
        for k in range(1000, 10000):
            if 2*k*k-1105*k+503388 >= n:
                return find(n-2*k*k+1109*k-504495)
    for k in range(10001, 100000):
        if (5*k*k-22207*k)//2+50488389 >= n:
            return find(n-(5*k-22212)*(k-1)//2-50488389)


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
