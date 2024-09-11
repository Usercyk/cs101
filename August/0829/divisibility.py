n = int(input())

for _ in range(n):
    a, b = map(int, input().split(" "))
    print(b-a % b if a % b else 0)
