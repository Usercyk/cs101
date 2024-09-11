feet = int(input())

if feet % 2 == 1:
    print(0, 0)
else:
    min_head = feet//4+(feet % 4) // 2
    max_head = feet//2
    print(min_head, max_head)
