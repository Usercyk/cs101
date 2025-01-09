from collections import defaultdict

nums = {"M": 1_000_000, "B": 1_000_000_000}


def transform(s):
    return float(s[:-1]) * nums[s[-1]]


d = defaultdict(list)
for _ in range(int(input())):
    name, cnt = input().split("-")
    d[name].append(cnt)
for k in sorted(d.keys()):
    d[k].sort(key=transform)
    print(f"{k}: {', '.join(d[k])}")
