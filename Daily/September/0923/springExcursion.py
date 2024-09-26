ran = range(1, int(input())+1)
ls = sorted(map(int, input().split()))
print(*(i for i in ran if i not in ls))
print(*(i for i in ls if i not in ran))
