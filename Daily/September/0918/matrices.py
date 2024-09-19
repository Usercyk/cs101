def getMatrices():
    matrices = [[], [], []]
    for i in range(3):
        row, _ = map(int, input().split())
        for _ in range(row):
            matrices[i].append(list(map(int, input().split())))
    return matrices


def times(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b)))) for j in range(len(b[0]))] for i in range(len(a))]


def plus(c, d):
    return [[c[i][j]+d[i][j] for j in range(len(c[0]))] for i in range(len(c))]


def main():
    a, b, c = getMatrices()
    if not (len(a[0]) == len(b) and len(a) == len(c) and len(b[0]) == len(c[0])):
        print("Error!")
        return
    s = plus(c, times(a, b))
    for p in s:
        print(*p)


main()
