s = input().replace(".", "0").replace("#", "1")
n = len(s)
num = int(f"0b{s}", 2)

tem = bin((num ^ (num << 1)))[2:].rjust(n, "0")

nxorRes = list(map(lambda x: 1-int(x), tem[-n:-1]+"1"))

prefixSum = []  # prefixSum[i]: 0<= <i

for i in range(n):
    if i == 0:
        prefixSum.append(0)
    else:
        prefixSum.append(prefixSum[i-1]+nxorRes[i-1])

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(prefixSum[r-1]-prefixSum[l-1])
