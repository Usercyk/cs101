t = int(input())
for _ in range(t):
    input()
    print(*(i[1] for i in sorted(zip(sorted(enumerate(map(int, input().split())),
          key=lambda x: x[1]), sorted(map(int, input().split()))), key=lambda x: x[0][0])))
