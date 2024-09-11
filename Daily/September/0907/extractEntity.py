import re
n = int(input())
pattern = "###(.*?)###"
ans = 0

for _ in range(n):
    words = input().replace("### ###", " ")
    count = len(re.findall(pattern, words))
    ans += count

print(ans)
