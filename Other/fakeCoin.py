balToRes = {"up": 1, "even": 0, "down": -1}

for _ in range(int(input())):
    a = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [],
         'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []}
    res = []
    reverse_res = []

    for _ in range(3):
        left, right, bal = input().split(" ")[:3]

        for k in a:
            if k in left:
                a[k].append(1)
            elif k in right:
                a[k].append(-1)
            else:
                a[k].append(0)
        res.append(balToRes[bal])
        reverse_res.append(-balToRes[bal])

    for k, v in a.items():
        if v == res:
            print(f"{k} is the counterfeit coin and it is heavy.")
            break
        elif v == reverse_res:
            print(f"{k} is the counterfeit coin and it is light.")
            break
