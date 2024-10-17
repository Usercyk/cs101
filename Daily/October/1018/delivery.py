for _ in range(int(input())):
    n = int(input())
    p = sorted(zip(map(int, input().split()), map(int, input().split())))
    suffix_sum = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        suffix_sum[i] = suffix_sum[i+1]+p[i][1]
    print(min(*(max(p[i][0], suffix_sum[i+1])
          for i in range(n)), suffix_sum[0]))
